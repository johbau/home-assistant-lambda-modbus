import ipaddress
import re

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_HOST, CONF_PORT, CONF_SCAN_INTERVAL
from .const import (
    DOMAIN,
    DEFAULT_NAME,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_PORT,
    DEFAULT_MODBUS_ADDRESS,
    CONF_MODBUS_ADDRESS,
    CONF_ENERGY_MANAGER,
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
    DEFAULT_READ_HP1,
    DEFAULT_READ_HP2,
    DEFAULT_READ_HP3,
    DEFAULT_READ_BOILER1,
    DEFAULT_READ_BOILER2,
    DEFAULT_READ_BOILER3,
    DEFAULT_READ_BOILER4,
    DEFAULT_READ_BOILER5,
    DEFAULT_READ_BUFFER1,
    DEFAULT_READ_BUFFER2,
    DEFAULT_READ_BUFFER3,
    DEFAULT_READ_BUFFER4,
    DEFAULT_READ_BUFFER5,
    DEFAULT_READ_SOLAR1,
    DEFAULT_READ_SOLAR2,
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
)
# Heat circuit configuration
CONF_HEAT_CIRCUIT1 = "read_hc1"
CONF_HEAT_CIRCUIT2 = "read_hc2"
CONF_HEAT_CIRCUIT3 = "read_hc3"
CONF_HEAT_CIRCUIT4 = "read_hc4"

DEFAULT_HEAT_CIRCUIT1 = True
DEFAULT_HEAT_CIRCUIT2 = True
DEFAULT_HEAT_CIRCUIT3 = True
DEFAULT_HEAT_CIRCUIT4 = True

from homeassistant.core import HomeAssistant, callback

DATA_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): str,
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
        vol.Optional(CONF_MODBUS_ADDRESS, default=DEFAULT_MODBUS_ADDRESS): int,
        vol.Optional(CONF_ENERGY_MANAGER, default=DEFAULT_ENERGY_MANAGER): bool,
        vol.Optional(CONF_READ_HP1, default=DEFAULT_READ_HP1): bool,
        vol.Optional(CONF_READ_HP2, default=DEFAULT_READ_HP2): bool,
        vol.Optional(CONF_READ_HP3, default=DEFAULT_READ_HP3): bool,
        vol.Optional(CONF_READ_BOILER1, default=DEFAULT_READ_BOILER1): bool,
        vol.Optional(CONF_READ_BOILER2, default=DEFAULT_READ_BOILER2): bool,
        vol.Optional(CONF_READ_BOILER3, default=DEFAULT_READ_BOILER3): bool,
        vol.Optional(CONF_READ_BOILER4, default=DEFAULT_READ_BOILER4): bool,
        vol.Optional(CONF_READ_BOILER5, default=DEFAULT_READ_BOILER5): bool,
        vol.Optional(CONF_READ_BUFFER1, default=DEFAULT_READ_BUFFER1): bool,
        vol.Optional(CONF_READ_BUFFER2, default=DEFAULT_READ_BUFFER2): bool,
        vol.Optional(CONF_READ_BUFFER3, default=DEFAULT_READ_BUFFER3): bool,
        vol.Optional(CONF_READ_BUFFER4, default=DEFAULT_READ_BUFFER4): bool,
        vol.Optional(CONF_READ_BUFFER5, default=DEFAULT_READ_BUFFER5): bool,
        vol.Optional(CONF_READ_SOLAR1, default=DEFAULT_READ_SOLAR1): bool,
        vol.Optional(CONF_READ_SOLAR2, default=DEFAULT_READ_SOLAR2): bool,
        vol.Optional(CONF_READ_HC1, default=DEFAULT_READ_HC1): bool,
        vol.Optional(CONF_READ_HC2, default=DEFAULT_READ_HC2): bool,
        vol.Optional(CONF_READ_HC3, default=DEFAULT_READ_HC3): bool,
        vol.Optional(CONF_READ_HC4, default=DEFAULT_READ_HC4): bool,
        vol.Optional(CONF_READ_HC5, default=DEFAULT_READ_HC5): bool,
        vol.Optional(CONF_READ_HC6, default=DEFAULT_READ_HC6): bool,
        vol.Optional(CONF_READ_HC7, default=DEFAULT_READ_HC7): bool,
        vol.Optional(CONF_READ_HC8, default=DEFAULT_READ_HC8): bool,
        vol.Optional(CONF_READ_HC9, default=DEFAULT_READ_HC9): bool,
        vol.Optional(CONF_READ_HC10, default=DEFAULT_READ_HC10): bool,
        vol.Optional(CONF_READ_HC11, default=DEFAULT_READ_HC11): bool,
        vol.Optional(CONF_READ_HC12, default=DEFAULT_READ_HC12): bool,
        vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): int,
    }
)


def host_valid(host):
    """Return True if hostname or IP address is valid."""
    try:
        if ipaddress.ip_address(host).version == (4 or 6):
            return True
    except ValueError:
        disallowed = re.compile(r"[^a-zA-Z\d\-]")
        return all(x and not disallowed.search(x) for x in host.split("."))


@callback
def lambda_modbus_entries(hass: HomeAssistant):
    """Return the hosts already configured."""
    return set(
        entry.data[CONF_HOST] for entry in hass.config_entries.async_entries(DOMAIN)
    )


class LambdaModbusConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Lambda Modbus configflow."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    def _host_in_configuration_exists(self, host) -> bool:
        """Return True if host exists in configuration."""
        if host in lambda_modbus_entries(self.hass):
            return True
        return False

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            host = user_input[CONF_HOST]

            if self._host_in_configuration_exists(host):
                errors[CONF_HOST] = "already_configured"
            elif not host_valid(user_input[CONF_HOST]):
                errors[CONF_HOST] = "invalid host IP"
            else:
                await self.async_set_unique_id(user_input[CONF_HOST])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=user_input[CONF_NAME], data=user_input
                )

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )
