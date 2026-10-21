"""Minimal Lambda heat pump Modbus TCP simulator.

Usage: .venv/bin/python scripts/simulator.py [--port 5020]
Then point the integration (or HA dev instance) at 127.0.0.1:<port>.
"""
import argparse
import asyncio

from pymodbus.server import StartAsyncTcpServer
from pymodbus.simulator import DataType, SimData, SimDevice

# ponytail: every holding register 0..6299 returns the same value (215 -> 21.5 / 2.15),
# enough to exercise all modules; add per-register values when testing decoding/state mapping.
REGISTER_VALUE = 215
REGISTER_COUNT = 6300  # covers heat circuit 12 (6100) + 50 offset


def device(value=REGISTER_VALUE):
    return SimDevice(
        id=1,
        simdata=[SimData(address=0, count=REGISTER_COUNT, values=value, datatype=DataType.REGISTERS)],
    )


async def serve(host="127.0.0.1", port=5020):
    await StartAsyncTcpServer(device(), address=(host, port))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5020)
    args = parser.parse_args()
    asyncio.run(serve(args.host, args.port))
