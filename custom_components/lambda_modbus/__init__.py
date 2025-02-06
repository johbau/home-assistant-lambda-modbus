"""The Lambda Modbus Integration."""
import asyncio
import logging
import operator
import threading
from datetime import timedelta
from typing import Optional

import voluptuous as vol
from pymodbus.client import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

import homeassistant.helpers.config_validation as cv
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME, CONF_HOST, CONF_PORT, CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant
from homeassistant.core import callback
from homeassistant.helpers.event import async_track_time_interval
from .const import (
    DOMAIN,
    DEFAULT_NAME,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_MODBUS_ADDRESS,
    CONF_MODBUS_ADDRESS,
    CONF_ENERGY_MANAGER,
    AMBIENT_SENSOR_OPERATING_STATES,
    CONF_READ_HP1,
    CONF_READ_HP2,
    CONF_READ_HP3,
    CONF_READ_BOILER1,
    CONF_READ_BOILER2,
    CONF_READ_BOILER3,
    CONF_READ_BOILER4,
    CONF_READ_BOILER5,
    DEFAULT_ENERGY_MANAGER,
    ENERGY_MANAGER_OPERATING_STATES,
    DEFAULT_READ_HP1,
    DEFAULT_READ_HP2,
    DEFAULT_READ_HP3,
    HEAT_PUMP_ERROR_STATES,
    HEAT_PUMP_STATES,
    HEAT_PUMP_OPERATING_STATES,
    DEFAULT_READ_BOILER1,
    DEFAULT_READ_BOILER2,
    DEFAULT_READ_BOILER3,
    DEFAULT_READ_BOILER4,
    DEFAULT_READ_BOILER5,
    BOILER_OPERATING_STATES,
)

_LOGGER = logging.getLogger(__name__)

LAMBDA_MODBUS_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_HOST): cv.string,
        vol.Required(CONF_PORT): cv.string,
        vol.Optional(
            CONF_MODBUS_ADDRESS, default=DEFAULT_MODBUS_ADDRESS
        ): cv.positive_int,
        vol.Optional(CONF_ENERGY_MANAGER, default=DEFAULT_ENERGY_MANAGER): cv.boolean,
        vol.Optional(CONF_READ_HP1, default=DEFAULT_READ_HP1): cv.boolean,
        vol.Optional(CONF_READ_HP2, default=DEFAULT_READ_HP2): cv.boolean,
        vol.Optional(CONF_READ_HP3, default=DEFAULT_READ_HP3): cv.boolean,
        vol.Optional(CONF_READ_BOILER1, default=DEFAULT_READ_BOILER1): cv.boolean,
        vol.Optional(CONF_READ_BOILER2, default=DEFAULT_READ_BOILER2): cv.boolean,
        vol.Optional(CONF_READ_BOILER3, default=DEFAULT_READ_BOILER3): cv.boolean,
        vol.Optional(CONF_READ_BOILER4, default=DEFAULT_READ_BOILER4): cv.boolean,
        vol.Optional(CONF_READ_BOILER5, default=DEFAULT_READ_BOILER5): cv.boolean,
        vol.Optional(
            CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL
        ): cv.positive_int,
    }
)

CONFIG_SCHEMA = vol.Schema(
    {DOMAIN: vol.Schema({cv.slug: LAMBDA_MODBUS_SCHEMA})}, extra=vol.ALLOW_EXTRA
)

PLATFORMS = ["sensor"]


async def async_setup(hass, config):
    """Set up the Lambda modbus component."""
    hass.data[DOMAIN] = {}
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up a lambda mobus."""
    host = entry.data[CONF_HOST]
    name = entry.data[CONF_NAME]
    port = entry.data[CONF_PORT]
    address = entry.data.get(CONF_MODBUS_ADDRESS, 1)
    scan_interval = entry.data[CONF_SCAN_INTERVAL]
    energy_manager = entry.data.get(CONF_ENERGY_MANAGER, DEFAULT_ENERGY_MANAGER)
    read_hp1 = entry.data.get(CONF_READ_HP1, DEFAULT_READ_HP1)
    read_hp2 = entry.data.get(CONF_READ_HP2, DEFAULT_READ_HP2)
    read_hp3 = entry.data.get(CONF_READ_HP3, DEFAULT_READ_HP3)
    read_boiler1 = entry.data.get(CONF_READ_BOILER1, DEFAULT_READ_BOILER1)
    read_boiler2 = entry.data.get(CONF_READ_BOILER2, DEFAULT_READ_BOILER2)
    read_boiler3 = entry.data.get(CONF_READ_BOILER3, DEFAULT_READ_BOILER3)
    read_boiler4 = entry.data.get(CONF_READ_BOILER4, DEFAULT_READ_BOILER4)
    read_boiler5 = entry.data.get(CONF_READ_BOILER5, DEFAULT_READ_BOILER5)

    _LOGGER.debug("Setup %s.%s", DOMAIN, name)

    hub = LambdaModbusHub(
        hass,
        name,
        host,
        port,
        address,
        scan_interval,
        energy_manager,
        read_hp1,
        read_hp2,
        read_hp3,
        read_boiler1,
        read_boiler2,
        read_boiler3,
        read_boiler4,
        read_boiler5,
    )
    """Register the hub."""
    hass.data[DOMAIN][name] = {"hub": hub}

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass, entry):
    """Unload Lambda mobus entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in PLATFORMS
            ]
        )
    )
    if not unload_ok:
        return False

    hass.data[DOMAIN].pop(entry.data["name"])
    return True


def validate(value, comparison, against):
    ops = {
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne,
    }
    if not ops[comparison](value, against):
        raise ValueError(f"Value {value} failed validation ({comparison}{against})")
    return value


class LambdaModbusHub:
    """Thread safe wrapper class for pymodbus."""

    def __init__(
            self,
            hass,
            name,
            host,
            port,
            address,
            scan_interval,
            energy_manager=DEFAULT_ENERGY_MANAGER,
            read_hp1=DEFAULT_READ_HP1,
            read_hp2=DEFAULT_READ_HP2,
            read_hp3=DEFAULT_READ_HP3,
            read_boiler1=DEFAULT_READ_BOILER1,
            read_boiler2=DEFAULT_READ_BOILER2,
            read_boiler3=DEFAULT_READ_BOILER3,
            read_boiler4=DEFAULT_READ_BOILER4,
            read_boiler5=DEFAULT_READ_BOILER5,
    ):
        """Initialize the Modbus hub."""
        self._hass = hass
        self._client = ModbusTcpClient(host=host, port=port, timeout=max(3, (scan_interval - 1)))
        self._lock = threading.Lock()
        self._name = name
        self._address = address
        self.energy_manager = energy_manager
        self.read_hp1 = read_hp1
        self.read_hp2 = read_hp2
        self.read_hp3 = read_hp3
        self.read_boiler1 = read_boiler1
        self.read_boiler2 = read_boiler2
        self.read_boiler3 = read_boiler3
        self.read_boiler4 = read_boiler4
        self.read_boiler5 = read_boiler5
        self._scan_interval = timedelta(seconds=scan_interval)
        self._unsub_interval_method = None
        self._sensors = []
        self.data = {}

    @callback
    def async_add_lambda_sensor(self, update_callback):
        """Listen for data updates."""
        # This is the first sensor, set up interval.
        if not self._sensors:
            # self.connect()
            self._unsub_interval_method = async_track_time_interval(
                self._hass, self.async_refresh_modbus_data, self._scan_interval
            )

        self._sensors.append(update_callback)

    @callback
    def async_remove_lambda_sensor(self, update_callback):
        """Remove data update."""
        self._sensors.remove(update_callback)

        if not self._sensors:
            """stop the interval timer upon removal of last sensor"""
            self._unsub_interval_method()
            self._unsub_interval_method = None
            self.close()

    async def async_refresh_modbus_data(self, _now: Optional[int] = None) -> dict:
        """Time to update."""
        result : bool = await self._hass.async_add_executor_job(self._refresh_modbus_data)
        if result:
            for update_callback in self._sensors:
                update_callback()


    def _refresh_modbus_data(self, _now: Optional[int] = None) -> bool:
        """Time to update."""
        if not self._sensors:
            return False

        if not self._check_and_reconnect():
            #if not connected, skip
            return False

        try:
            update_result = self.read_modbus_data()
        except Exception as e:
            _LOGGER.exception("Error reading modbus data", exc_info=True)
            update_result = False
        return update_result



    @property
    def name(self):
        """Return the name of this hub."""
        return self._name

    def close(self):
        """Disconnect client."""
        with self._lock:
            self._client.close()

    def _check_and_reconnect(self):
        if not self._client.connected:
            _LOGGER.info("modbus client is not connected, trying to reconnect")
            return self.connect()

        return self._client.connected

    def connect(self):
        """Connect client."""
        result = False
        with self._lock:
            result = self._client.connect()

        if result:
            _LOGGER.info("successfully connected to %s:%s",
                         self._client.comm_params.host, self._client.comm_params.port)
        else:
            _LOGGER.warning("not able to connect to %s:%s",
                            self._client.comm_params.host, self._client.comm_params.port)
        return result


    @property
    def energy_manager_enabled(self):
        """Return true if energy manager has been enabled"""
        return self.energy_manager

    @property
    def has_heat_pump(self):
        """Return true if a meter is available"""
        return self.read_hp1 or self.read_hp2 or self.read_hp3

    @property
    def has_boiler(self):
        """Return true if a boiler is available"""
        return self.read_boiler1 or self.read_boiler2 or self.read_boiler3 or self.read_boiler4 or self.read_boiler5

    def read_holding_registers(self, unit, address, count):
        """Read holding registers."""
        with self._lock:
            return self._client.read_holding_registers(
                address=address, count=count, slave=unit
            )

    def write_registers(self, unit, address, payload):
        """Write registers."""
        with self._lock:
            return self._client.write_registers(
                address=address, values=payload, slave=unit
            )

    def read_modbus_data(self):
        return (
                self.read_modbus_data_ambient()
                and self.read_modbus_data_energy_manager()
                and self.read_modbus_data_heat_pump1()
                and self.read_modbus_data_heat_pump2()
                and self.read_modbus_data_heat_pump3()
                and self.read_modbus_data_boiler1()
                and self.read_modbus_data_boiler2()
                and self.read_modbus_data_boiler3()
                and self.read_modbus_data_boiler4()
                and self.read_modbus_data_boiler5()
        )

    def read_modbus_data_ambient(self):
        ambient_data = self.read_holding_registers(
            unit=self._address, address=0, count=5
        )
        if ambient_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            ambient_data.registers, byteorder=Endian.BIG
        )
        self.data["error_number"] = decoder.decode_16bit_int()
        operating_state = decoder.decode_16bit_uint()
        if operating_state in AMBIENT_SENSOR_OPERATING_STATES:
            self.data["operating_state"] = AMBIENT_SENSOR_OPERATING_STATES[operating_state]
        else:
            self.data["operating_state"] = operating_state
        self.data["temperature"] = decoder.decode_16bit_int() / 10
        self.data["temperature_1h"] = decoder.decode_16bit_int() / 10
        self.data["temperature_calculated"] = decoder.decode_16bit_int() / 10
        return True

    def read_modbus_data_energy_manager(self):
        if not self.energy_manager_enabled:
            return True

        energy_manager_data = self.read_holding_registers(
            unit=self._address, address=100, count=5
        )
        if energy_manager_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            energy_manager_data.registers, byteorder=Endian.BIG
        )
        self.data["error_number"] = decoder.decode_16bit_int()
        operating_state = decoder.decode_16bit_uint()
        if operating_state in ENERGY_MANAGER_OPERATING_STATES:
            self.data["operating_state"] = ENERGY_MANAGER_OPERATING_STATES[operating_state]
        else:
            self.data["operating_state"] = operating_state
        self.data["actual_power"] = decoder.decode_16bit_uint()
        self.data["actual_power_consumption"] = decoder.decode_16bit_int()
        self.data["setpoint_power_consumption"] = decoder.decode_16bit_int()
        return True

    def read_modbus_data_heat_pump1(self):
        if self.read_hp1:
            return self.read_modbus_data_heat_pump("hp1_", 1000)
        return True

    def read_modbus_data_heat_pump2(self):
        if self.read_hp2:
            return self.read_modbus_data_heat_pump("hp2_", 1100)
        return True

    def read_modbus_data_heat_pump3(self):
        if self.read_hp3:
            return self.read_modbus_data_heat_pump("hp3_", 1200)
        return True

    def read_modbus_data_heat_pump(self, heat_pump_prefix, start_address):
        """start reading heat pump data"""
        heat_pump_data = self.read_holding_registers(
            unit=self._address, address=start_address, count=24
        )
        if heat_pump_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            heat_pump_data.registers, byteorder=Endian.BIG
        )
        error_state = decoder.decode_16bit_uint()
        if error_state in HEAT_PUMP_ERROR_STATES:
            self.data[heat_pump_prefix + "error_state"] = HEAT_PUMP_ERROR_STATES[error_state]
        else:
            self.data[heat_pump_prefix + "error_state"] = error_state
        self.data[heat_pump_prefix + "error_number"] = decoder.decode_16bit_int()
        state = decoder.decode_16bit_uint()
        if error_state in HEAT_PUMP_STATES:
            self.data[heat_pump_prefix + "state"] = HEAT_PUMP_STATES[state]
        else:
            self.data[heat_pump_prefix + "state"] = state
        operating_state = decoder.decode_16bit_uint()
        if operating_state in HEAT_PUMP_OPERATING_STATES:
            self.data[heat_pump_prefix + "operating_state"] = HEAT_PUMP_OPERATING_STATES[operating_state]
        else:
            self.data[heat_pump_prefix + "operating_state"] = operating_state
        self.data[heat_pump_prefix + "flow_line_temperature"] = decoder.decode_16bit_int() / 100
        self.data[heat_pump_prefix + "return_line_temperature"] = decoder.decode_16bit_int() / 100
        self.data[heat_pump_prefix + "heat_sink_volume_flow"] = decoder.decode_16bit_int() / 100
        self.data[heat_pump_prefix + "energy_source_inlet_temperature"] = decoder.decode_16bit_int() / 100
        self.data[heat_pump_prefix + "energy_source_outlet_temperature"] = decoder.decode_16bit_int() / 100
        self.data[heat_pump_prefix + "energy_source_volume_flow"] = decoder.decode_16bit_int() / 100
        self.data[heat_pump_prefix + "compressor_unit_rating"] = decoder.decode_16bit_uint() / 100
        self.data[heat_pump_prefix + "actual_heating_capacity"] = decoder.decode_16bit_int() / 10
        self.data[heat_pump_prefix + "inverter_power_consumption"] = decoder.decode_16bit_int()
        self.data[heat_pump_prefix + "cop"] = decoder.decode_16bit_int() / 100
        self.data[heat_pump_prefix + "request_release_password_register"] = decoder.decode_16bit_uint()
        self.data[heat_pump_prefix + "request_type"] = decoder.decode_16bit_int()
        self.data[heat_pump_prefix + "requested_flow_line_temperature"] = decoder.decode_16bit_int() / 10
        self.data[heat_pump_prefix + "requested_return_line_temperature"] = decoder.decode_16bit_int() / 10
        self.data[heat_pump_prefix + "requested_heat_sink_temperature_difference"] = decoder.decode_16bit_int() / 10
        self.data[heat_pump_prefix + "heating_stage_relais_state"] = decoder.decode_16bit_int()
        self.data[heat_pump_prefix + "compressor_power_consumption_accumulated"] = decoder.decode_32bit_uint()
        self.data[heat_pump_prefix + "compressor_thermal_power_output_accumulated"] = decoder.decode_32bit_uint()
        return True

    def read_modbus_data_boiler1(self):
        if self.read_boiler1:
            return self.read_modbus_data_boiler("boiler1_", 2000)
        return True

    def read_modbus_data_boiler2(self):
        if self.read_boiler2:
            return self.read_modbus_data_boiler("boiler2_", 2100)
        return True

    def read_modbus_data_boiler3(self):
        if self.read_boiler3:
            return self.read_modbus_data_boiler("boiler3_", 2200)
        return True

    def read_modbus_data_boiler4(self):
        if self.read_boiler4:
            return self.read_modbus_data_boiler("boiler4_", 2300)
        return True

    def read_modbus_data_boiler5(self):
        if self.read_boiler5:
            return self.read_modbus_data_boiler("boiler5_", 2400)
        return True

    def read_modbus_data_boiler(self, boiler_prefix, start_address):
        """start reading boiler data"""
        boiler_data = self.read_holding_registers(
            unit=self._address, address=start_address, count=4
        )
        if boiler_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            boiler_data.registers, byteorder=Endian.BIG
        )
        self.data[boiler_prefix + "error_number"] = decoder.decode_16bit_int()
        operating_state = decoder.decode_16bit_uint()
        if operating_state in BOILER_OPERATING_STATES:
            self.data[boiler_prefix + "operating_state"] = BOILER_OPERATING_STATES[operating_state]
        else:
            self.data[boiler_prefix + "operating_state"] = operating_state
        self.data[boiler_prefix + "high_temperature"] = decoder.decode_16bit_int() / 10
        self.data[boiler_prefix + "low_temperature"] = decoder.decode_16bit_int() / 10

        boiler_data = self.read_holding_registers(
            unit=self._address, address=start_address + 50, count=1
        )
        if boiler_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            boiler_data.registers, byteorder=Endian.BIG
        )
        self.data[boiler_prefix + "maximum_temperature"] = decoder.decode_16bit_int() / 10
        return True
