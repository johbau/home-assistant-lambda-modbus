import logging
from typing import Optional, Dict, Any
from .const import (
    AMBIENT_SENSOR_TYPES,
    ENERGY_MANAGER_SENSOR_TYPES,
    HP1_HEAT_PUMP_SENSOR_TYPES,
    HP2_HEAT_PUMP_SENSOR_TYPES,
    HP3_HEAT_PUMP_SENSOR_TYPES,
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
    for ambient_sensor_info in AMBIENT_SENSOR_TYPES.values():
        sensor = LambdaSensor(
            hub_name,
            hub,
            device_info,
            ambient_sensor_info[0],
            ambient_sensor_info[1],
            ambient_sensor_info[2],
            ambient_sensor_info[3],
        )
        entities.append(sensor)

    if hub.energy_manager == True:
        for energy_manager_sensor_info in ENERGY_MANAGER_SENSOR_TYPES.values():
            sensor = LambdaSensor(
                hub_name,
                hub,
                device_info,
                energy_manager_sensor_info[0],
                energy_manager_sensor_info[1],
                energy_manager_sensor_info[2],
                energy_manager_sensor_info[3],
            )
            entities.append(sensor)

    if hub.read_hp1 == True:
        for heat_pump_sensor_info in HP1_HEAT_PUMP_SENSOR_TYPES.values():
            sensor = LambdaSensor(
                hub_name,
                hub,
                device_info,
                heat_pump_sensor_info[0],
                heat_pump_sensor_info[1],
                heat_pump_sensor_info[2],
                heat_pump_sensor_info[3],
            )
            entities.append(sensor)

    if hub.read_hp2 == True:
        for heat_pump_sensor_info in HP2_HEAT_PUMP_SENSOR_TYPES.values():
            sensor = LambdaSensor(
                hub_name,
                hub,
                device_info,
                heat_pump_sensor_info[0],
                heat_pump_sensor_info[1],
                heat_pump_sensor_info[2],
                heat_pump_sensor_info[3],
            )
            entities.append(sensor)

    if hub.read_hp3 == True:
        for heat_pump_sensor_info in HP3_HEAT_PUMP_SENSOR_TYPES.values():
            sensor = LambdaSensor(
                hub_name,
                hub,
                device_info,
                heat_pump_sensor_info[0],
                heat_pump_sensor_info[1],
                heat_pump_sensor_info[2],
                heat_pump_sensor_info[3],
            )
            entities.append(sensor)

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
