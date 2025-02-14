import logging
from typing import Optional, Dict, Any
from .const import (
    AMBIENT_SENSOR_TYPES,
    ENERGY_MANAGER_SENSOR_TYPES,
    HP1_HEAT_PUMP_SENSOR_TYPES,
    HP2_HEAT_PUMP_SENSOR_TYPES,
    HP3_HEAT_PUMP_SENSOR_TYPES,
    BOILER1_SENSOR_TYPES,
    BOILER2_SENSOR_TYPES,
    BOILER3_SENSOR_TYPES,
    BOILER4_SENSOR_TYPES,
    BOILER5_SENSOR_TYPES,
    BUFFER1_SENSOR_TYPES,
    BUFFER2_SENSOR_TYPES,
    BUFFER3_SENSOR_TYPES,
    BUFFER4_SENSOR_TYPES,
    BUFFER5_SENSOR_TYPES,
    SOLAR1_SENSOR_TYPES,
    SOLAR2_SENSOR_TYPES,
    HC1_HEAT_CIRCUIT_SENSOR_TYPES,
    HC2_HEAT_CIRCUIT_SENSOR_TYPES,
    HC3_HEAT_CIRCUIT_SENSOR_TYPES,
    HC4_HEAT_CIRCUIT_SENSOR_TYPES,
    HC5_HEAT_CIRCUIT_SENSOR_TYPES,
    HC6_HEAT_CIRCUIT_SENSOR_TYPES,
    HC7_HEAT_CIRCUIT_SENSOR_TYPES,
    HC8_HEAT_CIRCUIT_SENSOR_TYPES,
    HC9_HEAT_CIRCUIT_SENSOR_TYPES,
    HC10_HEAT_CIRCUIT_SENSOR_TYPES,
    HC11_HEAT_CIRCUIT_SENSOR_TYPES,
    HC12_HEAT_CIRCUIT_SENSOR_TYPES,
    DOMAIN,
    ATTR_MANUFACTURER,
)
from datetime import datetime
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME, UnitOfEnergy, UnitOfPower
from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass
)

from homeassistant.core import callback
from homeassistant.util import dt as dt_util

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    hub_name = entry.data[CONF_NAME]
    hub = hass.data[DOMAIN][hub_name]["hub"]

    device_info = {
        "identifiers": {(DOMAIN, hub_name)},
        "name": hub_name,
        "manufacturer": ATTR_MANUFACTURER,
    }

    entities = []
    def add_sensors(sensor_types):
        for sensor_info in sensor_types.values():
            sensor = LambdaSensor(
                hub_name,
                hub,
                device_info,
                sensor_info[0],
                sensor_info[1],
                sensor_info[2],
                sensor_info[3],
            )
            entities.append(sensor)

    add_sensors(AMBIENT_SENSOR_TYPES)

    if hub.energy_manager:
        add_sensors(ENERGY_MANAGER_SENSOR_TYPES)

    if hub.read_hp1:
        add_sensors(HP1_HEAT_PUMP_SENSOR_TYPES)

    if hub.read_hp2:
        add_sensors(HP2_HEAT_PUMP_SENSOR_TYPES)

    if hub.read_hp3:
        add_sensors(HP3_HEAT_PUMP_SENSOR_TYPES)

    if hub.read_boiler1:
        add_sensors(BOILER1_SENSOR_TYPES)

    if hub.read_boiler2:
        add_sensors(BOILER2_SENSOR_TYPES)

    if hub.read_boiler3:
        add_sensors(BOILER3_SENSOR_TYPES)

    if hub.read_boiler4:
        add_sensors(BOILER4_SENSOR_TYPES)

    if hub.read_boiler5:
        add_sensors(BOILER5_SENSOR_TYPES)

    if hub.read_buffer1:
        add_sensors(BUFFER1_SENSOR_TYPES)

    if hub.read_buffer2:
        add_sensors(BUFFER2_SENSOR_TYPES)

    if hub.read_buffer3:
        add_sensors(BUFFER3_SENSOR_TYPES)

    if hub.read_buffer4:
        add_sensors(BUFFER4_SENSOR_TYPES)

    if hub.read_buffer5:
        add_sensors(BUFFER5_SENSOR_TYPES)

    if hub.read_solar1:
        add_sensors(SOLAR1_SENSOR_TYPES)

    if hub.read_solar2:
        add_sensors(SOLAR2_SENSOR_TYPES)

    # Add HC sensors
    if hub.read_hc1:
        add_sensors(HC1_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc2:
        add_sensors(HC2_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc3:
        add_sensors(HC3_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc4:
        add_sensors(HC4_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc5:
        add_sensors(HC5_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc6:
        add_sensors(HC6_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc7:
        add_sensors(HC7_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc8:
        add_sensors(HC8_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc9:
        add_sensors(HC9_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc10:
        add_sensors(HC10_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc11:
        add_sensors(HC11_HEAT_CIRCUIT_SENSOR_TYPES)
    if hub.read_hc12:
        add_sensors(HC12_HEAT_CIRCUIT_SENSOR_TYPES)

    async_add_entities(entities)
    return True


class LambdaSensor(SensorEntity):
    """Representation of an Lambda Modbus sensor."""

    def __init__(self, platform_name, hub, device_info, name, key, unit, icon):
        """Initialize the sensor."""
        self._platform_name = platform_name
        self._hub = hub
        self._key = key
        self._name = name
        self._unit_of_measurement = unit
        self._icon = icon
        self._device_info = device_info
        self._attr_state_class = SensorStateClass.MEASUREMENT
        if self._unit_of_measurement == UnitOfEnergy.KILO_WATT_HOUR :
            self._attr_state_class = SensorStateClass.TOTAL_INCREASING
            self._attr_device_class = SensorDeviceClass.ENERGY
        if self._unit_of_measurement == UnitOfPower.WATT :
            self._attr_device_class = SensorDeviceClass.POWER

    async def async_added_to_hass(self):
        """Register callbacks."""
        self._hub.async_add_lambda_sensor(self._modbus_data_updated)

    async def async_will_remove_from_hass(self) -> None:
        self._hub.async_remove_lambda_sensor(self._modbus_data_updated)

    @callback
    def _modbus_data_updated(self):
        self.async_write_ha_state()

    @callback
    def _update_state(self):
        if self._key in self._hub.data:
            self._state = self._hub.data[self._key]

    @property
    def name(self):
        """Return the name."""
        return f"{self._platform_name} ({self._name})"

    @property
    def unique_id(self) -> Optional[str]:
        return f"{self._platform_name}_{self._key}"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return the sensor icon."""
        return self._icon

    @property
    def state(self):
        """Return the state of the sensor."""
        if self._key in self._hub.data:
            return self._hub.data[self._key]

    @property
    def extra_state_attributes(self):
        return None

    @property
    def should_poll(self) -> bool:
        """Data is delivered by the hub"""
        return False

    @property
    def device_info(self) -> Optional[Dict[str, Any]]:
        return self._device_info
