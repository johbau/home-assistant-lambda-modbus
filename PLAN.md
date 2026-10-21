# Plan: catch up with home-assistant-solaredge-modbus

Lambda was built on the SolarEdge integration as it was before Jan 2025. SolarEdge has since moved to
`DataUpdateCoordinator`, `SensorEntityDescription`, `AsyncModbusTcpClient`, added a reconfigure flow and
fixed pymodbus/HA 2026.7 compatibility. This plan brings Lambda up to date in three releases.

## v0.7.4 – hotfix (committed `b8f8ae0`, not yet tagged)

V0.7.3 could not read any data. Fixed:

- Sync `ModbusTcpClient` in an executor called the async `read_modbus_data()` without awaiting it
  → switched to `AsyncModbusTcpClient` with `asyncio.Lock`
- `slave=` keyword removed in pymodbus ≥ 3.11 → `device_id=`
- `pymodbus.pdu.pdu` → `pymodbus.pdu.utils` import (HA 2026.7)
- Heat circuit 1 reader was not `async` and missed `await`
- Energy manager / heat pump / boiler modules were read twice per scan
- Dead duplicate `read_modbus_data_solar1/2` (pointed at boiler range 2500/2600)
- pymodbus 3.13.1, min HA 2026.7.0

**Open:** test against the real heat pump, then tag `V0.7.4` and push.

## v0.8.0 – architecture port

Port from SolarEdge:

- `DataUpdateCoordinator` + `CoordinatorEntity` instead of the callback list and
  `async_track_time_interval`; raise `UpdateFailed`, close the connection on error and reconnect on next read
- `SensorEntityDescription` in `const.py` instead of tuples
  - **keep the keys identical** – `unique_id` is `f"{name}_{key}"` in both, so entities and history survive
  - `has_entity_name` changes friendly names from "Lambda (Ambient Temperature)" to
    "Lambda Ambient Temperature"; entity IDs stay
- `async_step_reconfigure` in the config flow (SolarEdge commit `0719bd5`) + strings/translations
- Unload: `async_unload_platforms` instead of deprecated `async_forward_entry_unload`, close the hub

Skipped:

- Device model / serial / sw version – no such registers known in the Lambda map
- `async_migrate_entry` – config data schema does not change, `VERSION` stays 1

## v0.9.0 – PV surplus write entity

`number` entity for E-Manager register 102 (actual power, input or excess), based on SolarEdge `number.py`.
Source of the surplus value: the Shelly meter (instead of the SolarEdge meter).

Requirements from `doc/2025-02-13_Modbus-Beschreibung-und-Protokoll.pdf`:

- Registers xx00–xx49 time out after 5 min → re-send the value on every coordinator refresh
- Writes must use function code 0x10 (write multiple registers) – `write_registers`, not `write_register`
- E-Manager must be configured with the Modbus client as PV surplus source; the setting decides
  UINT16 (input power) vs INT16 (excess power) → reading register 102 must follow it
  (currently always decoded as UINT16)

Further writable registers (boiler/buffer max temperature, heat circuit setpoints/mode) only one at a time,
with min/max from the spec.

## Dev setup

See [scripts/README.md](scripts/README.md). Run `scripts/smoke_test.py` after every change.
