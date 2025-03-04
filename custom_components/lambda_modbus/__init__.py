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
    CONF_READ_BUFFER1,
    CONF_READ_BUFFER2,
    CONF_READ_BUFFER3,
    CONF_READ_BUFFER4,
    CONF_READ_BUFFER5,
    CONF_READ_SOLAR1,
    CONF_READ_SOLAR2,
    CONF_READ_HC1,
    CONF_READ_HC2,
    CONF_READ_HC3,
    CONF_READ_HC4,
    CONF_READ_HC5,
    CONF_READ_HC6,
    CONF_READ_HC7,
    CONF_READ_HC8,
    CONF_READ_HC9,
    CONF_READ_HC10,
    CONF_READ_HC11,
    CONF_READ_HC12,
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
    DEFAULT_READ_BUFFER1,
    DEFAULT_READ_BUFFER2,
    DEFAULT_READ_BUFFER3,
    DEFAULT_READ_BUFFER4,
    DEFAULT_READ_BUFFER5,
    BUFFER_OPERATING_STATES,
    BUFFER_REQUEST_TYPES,
    DEFAULT_READ_SOLAR1,
    DEFAULT_READ_SOLAR2,
    SOLAR_OPERATING_STATES,
    DEFAULT_READ_HC1,
    DEFAULT_READ_HC2,
    DEFAULT_READ_HC3,
    DEFAULT_READ_HC4,
    DEFAULT_READ_HC5,
    DEFAULT_READ_HC6,
    DEFAULT_READ_HC7,
    DEFAULT_READ_HC8,
    DEFAULT_READ_HC9,
    DEFAULT_READ_HC10,
    DEFAULT_READ_HC11,
    DEFAULT_READ_HC12,
    HC_OPERATING_STATES,
    HC_OPERATING_MODES,
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
        vol.Optional(CONF_READ_BUFFER1, default=DEFAULT_READ_BUFFER1): cv.boolean,
        vol.Optional(CONF_READ_BUFFER2, default=DEFAULT_READ_BUFFER2): cv.boolean,
        vol.Optional(CONF_READ_BUFFER3, default=DEFAULT_READ_BUFFER3): cv.boolean,
        vol.Optional(CONF_READ_BUFFER4, default=DEFAULT_READ_BUFFER4): cv.boolean,
        vol.Optional(CONF_READ_BUFFER5, default=DEFAULT_READ_BUFFER5): cv.boolean,
        vol.Optional(CONF_READ_SOLAR1, default=DEFAULT_READ_SOLAR1): cv.boolean,
        vol.Optional(CONF_READ_SOLAR2, default=DEFAULT_READ_SOLAR2): cv.boolean,
        vol.Optional(CONF_READ_HC1, default=DEFAULT_READ_HC1): cv.boolean,
        vol.Optional(CONF_READ_HC2, default=DEFAULT_READ_HC2): cv.boolean,
        vol.Optional(CONF_READ_HC3, default=DEFAULT_READ_HC3): cv.boolean,
        vol.Optional(CONF_READ_HC4, default=DEFAULT_READ_HC4): cv.boolean,
        vol.Optional(CONF_READ_HC5, default=DEFAULT_READ_HC5): cv.boolean,
        vol.Optional(CONF_READ_HC6, default=DEFAULT_READ_HC6): cv.boolean,
        vol.Optional(CONF_READ_HC7, default=DEFAULT_READ_HC7): cv.boolean,
        vol.Optional(CONF_READ_HC8, default=DEFAULT_READ_HC8): cv.boolean,
        vol.Optional(CONF_READ_HC9, default=DEFAULT_READ_HC9): cv.boolean,
        vol.Optional(CONF_READ_HC10, default=DEFAULT_READ_HC10): cv.boolean,
        vol.Optional(CONF_READ_HC11, default=DEFAULT_READ_HC11): cv.boolean,
        vol.Optional(CONF_READ_HC12, default=DEFAULT_READ_HC12): cv.boolean,
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
    read_buffer1 = entry.data.get(CONF_READ_BUFFER1, DEFAULT_READ_BUFFER1)
    read_buffer2 = entry.data.get(CONF_READ_BUFFER2, DEFAULT_READ_BUFFER2)
    read_buffer3 = entry.data.get(CONF_READ_BUFFER3, DEFAULT_READ_BUFFER3)
    read_buffer4 = entry.data.get(CONF_READ_BUFFER4, DEFAULT_READ_BUFFER4)
    read_buffer5 = entry.data.get(CONF_READ_BUFFER5, DEFAULT_READ_BUFFER5)
    read_solar1 = entry.data.get(CONF_READ_SOLAR1, DEFAULT_READ_SOLAR1)
    read_solar2 = entry.data.get(CONF_READ_SOLAR2, DEFAULT_READ_SOLAR2)
    read_hc1 = entry.data.get(CONF_READ_HC1, DEFAULT_READ_HC1)
    read_hc2 = entry.data.get(CONF_READ_HC2, DEFAULT_READ_HC2)
    read_hc3 = entry.data.get(CONF_READ_HC3, DEFAULT_READ_HC3)
    read_hc4 = entry.data.get(CONF_READ_HC4, DEFAULT_READ_HC4)
    read_hc5 = entry.data.get(CONF_READ_HC5, DEFAULT_READ_HC5)
    read_hc6 = entry.data.get(CONF_READ_HC6, DEFAULT_READ_HC6)
    read_hc7 = entry.data.get(CONF_READ_HC7, DEFAULT_READ_HC7)
    read_hc8 = entry.data.get(CONF_READ_HC8, DEFAULT_READ_HC8)
    read_hc9 = entry.data.get(CONF_READ_HC9, DEFAULT_READ_HC9)
    read_hc10 = entry.data.get(CONF_READ_HC10, DEFAULT_READ_HC10)
    read_hc11 = entry.data.get(CONF_READ_HC11, DEFAULT_READ_HC11)
    read_hc12 = entry.data.get(CONF_READ_HC12, DEFAULT_READ_HC12)

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
        read_buffer1,
        read_buffer2,
        read_buffer3,
        read_buffer4,
        read_buffer5,
        read_solar1,
        read_solar2,
        read_hc1,
        read_hc2,
        read_hc3,
        read_hc4,
        read_hc5,
        read_hc6,
        read_hc7,
        read_hc8,
        read_hc9,
        read_hc10,
        read_hc11,
        read_hc12,
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
            read_buffer1=DEFAULT_READ_BUFFER1,
            read_buffer2=DEFAULT_READ_BUFFER2,
            read_buffer3=DEFAULT_READ_BUFFER3,
            read_buffer4=DEFAULT_READ_BUFFER4,
            read_buffer5=DEFAULT_READ_BUFFER5,
            read_solar1=DEFAULT_READ_SOLAR1,
            read_solar2=DEFAULT_READ_SOLAR2,
            read_hc1=DEFAULT_READ_HC1,
            read_hc2=DEFAULT_READ_HC2,
            read_hc3=DEFAULT_READ_HC3,
            read_hc4=DEFAULT_READ_HC4,
            read_hc5=DEFAULT_READ_HC5,
            read_hc6=DEFAULT_READ_HC6,
            read_hc7=DEFAULT_READ_HC7,
            read_hc8=DEFAULT_READ_HC8,
            read_hc9=DEFAULT_READ_HC9,
            read_hc10=DEFAULT_READ_HC10,
            read_hc11=DEFAULT_READ_HC11,
            read_hc12=DEFAULT_READ_HC12,
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
        self.read_buffer1 = read_buffer1
        self.read_buffer2 = read_buffer2
        self.read_buffer3 = read_buffer3
        self.read_buffer4 = read_buffer4
        self.read_buffer5 = read_buffer5
        self.read_solar1 = read_solar1
        self.read_solar2 = read_solar2
        self.read_hc1 = read_hc1
        self.read_hc2 = read_hc2
        self.read_hc3 = read_hc3
        self.read_hc4 = read_hc4
        self.read_hc5 = read_hc5
        self.read_hc6 = read_hc6
        self.read_hc7 = read_hc7
        self.read_hc8 = read_hc8
        self.read_hc9 = read_hc9
        self.read_hc10 = read_hc10
        self.read_hc11 = read_hc11
        self.read_hc12 = read_hc12
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

    @property
    def has_buffer(self):
        """Return true if a boiler is available"""
        return self.read_buffer1 or self.read_buffer2 or self.read_buffer3 or self.read_buffer4 or self.read_buffer5

    def has_solar(self):
        """Return true if a solar is available"""
        return self.read_solar1 or self.read_solar2

    @property
    def has_heat_circuit(self):
        """Return true if a heat circuit is available"""
        return (
            self.read_hc1 or self.read_hc2 or self.read_hc3 or self.read_hc4 or
            self.read_hc5 or self.read_hc6 or self.read_hc7 or self.read_hc8 or
            self.read_hc9 or self.read_hc10 or self.read_hc11 or self.read_hc12
        )

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
                and self.read_modbus_data_buffer1()
                and self.read_modbus_data_buffer2()
                and self.read_modbus_data_buffer3()
                and self.read_modbus_data_buffer4()
                and self.read_modbus_data_buffer5()
                and self.read_modbus_data_solar1()
                and self.read_modbus_data_solar2()
                and self.read_modbus_data_energy_manager()
                and self.read_modbus_data_heat_pump1()
                and self.read_modbus_data_heat_pump2()
                and self.read_modbus_data_heat_pump3()
                and self.read_modbus_data_boiler1()
                and self.read_modbus_data_boiler2()
                and self.read_modbus_data_boiler3()
                and self.read_modbus_data_boiler4()
                and self.read_modbus_data_boiler5()
                and self.read_modbus_data_heat_circuit1()
                and self.read_modbus_data_heat_circuit2()
                and self.read_modbus_data_heat_circuit3()
                and self.read_modbus_data_heat_circuit4()
                and self.read_modbus_data_heat_circuit5()
                and self.read_modbus_data_heat_circuit6()
                and self.read_modbus_data_heat_circuit7()
                and self.read_modbus_data_heat_circuit8()
                and self.read_modbus_data_heat_circuit9()
                and self.read_modbus_data_heat_circuit10()
                and self.read_modbus_data_heat_circuit11()
                and self.read_modbus_data_heat_circuit12()
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
        self.data["ambient_error_number"] = decoder.decode_16bit_int()
        operating_state = decoder.decode_16bit_uint()
        if operating_state in AMBIENT_SENSOR_OPERATING_STATES:
            self.data["ambient_operating_state"] = AMBIENT_SENSOR_OPERATING_STATES[operating_state]
        else:
            self.data["ambient_operating_state"] = operating_state
        self.data["ambient_temperature"] = decoder.decode_16bit_int() / 10
        self.data["ambient_temperature_1h"] = decoder.decode_16bit_int() / 10
        self.data["ambient_temperature_calculated"] = decoder.decode_16bit_int() / 10
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
        self.data["energy_manager_error_number"] = decoder.decode_16bit_int()
        operating_state = decoder.decode_16bit_uint()
        if operating_state in ENERGY_MANAGER_OPERATING_STATES:
            self.data["energy_manager_operating_state"] = ENERGY_MANAGER_OPERATING_STATES[operating_state]
        else:
            self.data["energy_manager_operating_state"] = operating_state
        self.data["energy_manager_actual_power"] = decoder.decode_16bit_uint()
        self.data["energy_manager_actual_power_consumption"] = decoder.decode_16bit_int()
        self.data["energy_manager_setpoint_power_consumption"] = decoder.decode_16bit_int()
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

    def read_modbus_data_solar1(self):
        if self.read_solar1:
            return self.read_modbus_data_solar("solar1_", 2500)
        return True

    def read_modbus_data_solar2(self):
        if self.read_solar2:
            return self.read_modbus_data_solar("solar2_", 2600)
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

    def read_modbus_data_buffer1(self):
        if self.read_buffer1:
            return self.read_modbus_data_buffer("buffer1_", 3000)
        return True

    def read_modbus_data_buffer2(self):
        if self.read_buffer2:
            return self.read_modbus_data_buffer("buffer2_", 3100)
        return True

    def read_modbus_data_buffer3(self):
        if self.read_buffer3:
            return self.read_modbus_data_buffer("buffer3_", 3200)
        return True

    def read_modbus_data_buffer4(self):
        if self.read_buffer4:
            return self.read_modbus_data_buffer("buffer4_", 3300)
        return True

    def read_modbus_data_buffer5(self):
        if self.read_buffer5:
            return self.read_modbus_data_buffer("buffer5_", 3400)
        return True

    def read_modbus_data_buffer(self, buffer_prefix, start_address):
        """start reading buffer data"""
        buffer_data = self.read_holding_registers(
            unit=self._address, address=start_address, count=10
        )
        if buffer_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            buffer_data.registers, byteorder=Endian.BIG
        )
        self.data[buffer_prefix + "error_number"] = decoder.decode_16bit_int()
        operating_state = decoder.decode_16bit_uint()
        if operating_state in BUFFER_OPERATING_STATES:
            self.data[buffer_prefix + "operating_state"] = BOILER_OPERATING_STATES[operating_state]
        else:
            self.data[buffer_prefix + "operating_state"] = operating_state
        self.data[buffer_prefix + "high_temperature"] = decoder.decode_16bit_int() / 10
        self.data[buffer_prefix + "low_temperature"] = decoder.decode_16bit_int() / 10
        self.data[buffer_prefix + "modbus_temperature"] = decoder.decode_16bit_int() / 10
        request_type = decoder.decode_16bit_int()
        if request_type in BUFFER_REQUEST_TYPES:
            self.data[buffer_prefix + "request_type"] = BUFFER_REQUEST_TYPES[request_type]
        else:
            self.data[buffer_prefix + "request_type"] = request_type
        self.data[buffer_prefix + "requested_flow_temperature"] = decoder.decode_16bit_int() / 10
        self.data[buffer_prefix + "requested_return_temperature"] = decoder.decode_16bit_int() / 10
        self.data[buffer_prefix + "requested_temperature_difference"] = decoder.decode_16bit_int() / 10
        self.data[buffer_prefix + "requested_capacity"] = decoder.decode_16bit_int() / 10

        buffer_data = self.read_holding_registers(
            unit=self._address, address=start_address + 50, count=1
        )
        if buffer_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            buffer_data.registers, byteorder=Endian.BIG
        )
        self.data[buffer_prefix + "maximum_temperature"] = decoder.decode_16bit_int() / 10
        return True

    def read_modbus_data_solar1(self):
        if self.read_solar1:
            return self.read_modbus_data_solar("solar1_", 4000)
        return True

    def read_modbus_data_solar2(self):
        if self.read_solar2:
            return self.read_modbus_data_solar("solar2_", 4100)
        return True

    def read_modbus_data_solar(self, solar_prefix, start_address):
        """start reading solar data"""
        solar_data = self.read_holding_registers(
            unit=self._address, address=start_address, count=5
        )
        if solar_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            solar_data.registers, byteorder=Endian.BIG
        )

        # Error number
        self.data[solar_prefix + "error_number"] = decoder.decode_16bit_int()

        # Operating state
        operating_state = decoder.decode_16bit_uint()
        if operating_state in SOLAR_OPERATING_STATES:
            self.data[solar_prefix + "operating_state"] = SOLAR_OPERATING_STATES[operating_state]
        else:
            self.data[solar_prefix + "operating_state"] = operating_state

        # Temperatures
        self.data[solar_prefix + "collector_temperature"] = decoder.decode_16bit_int() / 10
        self.data[solar_prefix + "buffer1_temperature"] = decoder.decode_16bit_int() / 10
        self.data[solar_prefix + "buffer2_temperature"] = decoder.decode_16bit_int() / 10

        buffer_data = self.read_holding_registers(
            unit=self._address, address=start_address + 50, count=2
        )
        if buffer_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            buffer_data.registers, byteorder=Endian.BIG
        )
        self.data[solar_prefix + "maximum_buffer_temperature"] = decoder.decode_16bit_int() / 10
        self.data[solar_prefix + "buffer_changeover_temperature"] = decoder.decode_16bit_int() / 10

        return True

    def read_modbus_data_heat_circuit1(self):
        if self.read_hc1:
            return self.read_modbus_data_heat_circuit("hc1_", 5000)
        return True

    def read_modbus_data_heat_circuit2(self):
        if self.read_hc2:
            return self.read_modbus_data_heat_circuit("hc2_", 5100)
        return True

    def read_modbus_data_heat_circuit3(self):
        if self.read_hc3:
            return self.read_modbus_data_heat_circuit("hc3_", 5200)
        return True

    def read_modbus_data_heat_circuit4(self):
        if self.read_hc4:
            return self.read_modbus_data_heat_circuit("hc4_", 5300)
        return True

    def read_modbus_data_heat_circuit5(self):
        if self.read_hc5:
            return self.read_modbus_data_heat_circuit("hc5_", 5400)
        return True

    def read_modbus_data_heat_circuit6(self):
        if self.read_hc6:
            return self.read_modbus_data_heat_circuit("hc6_", 5500)
        return True

    def read_modbus_data_heat_circuit7(self):
        if self.read_hc7:
            return self.read_modbus_data_heat_circuit("hc7_", 5600)
        return True

    def read_modbus_data_heat_circuit8(self):
        if self.read_hc8:
            return self.read_modbus_data_heat_circuit("hc8_", 5700)
        return True

    def read_modbus_data_heat_circuit9(self):
        if self.read_hc9:
            return self.read_modbus_data_heat_circuit("hc9_", 5800)
        return True

    def read_modbus_data_heat_circuit10(self):
        if self.read_hc10:
            return self.read_modbus_data_heat_circuit("hc10_", 5900)
        return True

    def read_modbus_data_heat_circuit11(self):
        if self.read_hc11:
            return self.read_modbus_data_heat_circuit("hc11_", 6000)
        return True

    def read_modbus_data_heat_circuit12(self):
        if self.read_hc12:
            return self.read_modbus_data_heat_circuit("hc12_", 6100)
        return True

    def read_modbus_data_heat_circuit(self, heat_circuit_prefix, start_address):
        """start reading heat circuit data"""
        heat_circuit_data = self.read_holding_registers(
            unit=self._address, address=start_address, count=7
        )
        if heat_circuit_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            heat_circuit_data.registers, byteorder=Endian.BIG
        )
        self.data[heat_circuit_prefix + "error_number"] = decoder.decode_16bit_int()
        operating_state = decoder.decode_16bit_uint()
        if operating_state in HC_OPERATING_STATES:
            self.data[heat_circuit_prefix + "operating_state"] = HC_OPERATING_STATES[operating_state]
        else:
            self.data[heat_circuit_prefix + "operating_state"] = operating_state
        self.data[heat_circuit_prefix + "flow_line_temperature"] = decoder.decode_16bit_int() / 10
        self.data[heat_circuit_prefix + "return_line_temperature"] = decoder.decode_16bit_int() / 10
        self.data[heat_circuit_prefix + "room_device_temperature"] = decoder.decode_16bit_int() / 10
        self.data[heat_circuit_prefix + "setpoint_flow_line_temperature"] = decoder.decode_16bit_int() / 10
        operating_mode = decoder.decode_16bit_int()
        if operating_mode in HC_OPERATING_MODES:
            self.data[heat_circuit_prefix + "operating_mode"] = HC_OPERATING_MODES[operating_mode]
        else:
            self.data[heat_circuit_prefix + "operating_mode"] = operating_state

        heat_circuit_data = self.read_holding_registers(
            unit=self._address, address=start_address + 50, count=3
        )
        if heat_circuit_data.isError():
            return False

        decoder = BinaryPayloadDecoder.fromRegisters(
            heat_circuit_data.registers, byteorder=Endian.BIG
        )
        self.data[heat_circuit_prefix + "setpoint_offset_flow_line_temperature"] = decoder.decode_16bit_int() / 10
        self.data[heat_circuit_prefix + "setpoint_room_heating_temperature"] = decoder.decode_16bit_int() / 10
        self.data[heat_circuit_prefix + "setpoint_room_cooling_line_temperature"] = decoder.decode_16bit_int() / 10
        return True
