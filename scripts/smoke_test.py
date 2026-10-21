"""Read every module once from the simulator. Run: .venv/bin/python scripts/smoke_test.py"""
import asyncio
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from pymodbus.server import ServerAsyncStop

from custom_components.lambda_modbus import LambdaModbusHub
from simulator import serve

PORT = 15020
ALL = ["energy_manager"] + [
    f"read_{m}{i}"
    for m, n in (("hp", 3), ("boiler", 5), ("buffer", 5), ("solar", 2), ("hc", 12))
    for i in range(1, n + 1)
]


async def main():
    server = asyncio.create_task(serve(port=PORT))
    await asyncio.sleep(0.5)
    for latest_firmware in (False, True):
        hub = LambdaModbusHub(
            None, "lambda", "127.0.0.1", PORT, 1, 30,
            latest_firmware=latest_firmware, **{k: True for k in ALL},
        )
        assert await hub._check_and_reconnect()
        assert await hub.read_modbus_data() is True
        assert hub.data["ambient_temperature"] == 21.5, hub.data
        assert hub.data["hp3_flow_line_temperature"] == 2.15
        assert "hc1_operating_state" in hub.data
        assert "hc12_operating_state" in hub.data
        assert "solar2_operating_state" in hub.data
        await hub.close()
        print(f"latest_firmware={latest_firmware}: {len(hub.data)} values OK")
    await ServerAsyncStop()
    server.cancel()


asyncio.run(main())
