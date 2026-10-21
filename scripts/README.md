# Development: simulator and smoke test

## Setup

Home Assistant 2026.7 needs Python ≥ 3.13. The project venv uses Python 3.14 managed by `uv`, which is
installed into the venv itself (`.venv/bin/uv`).

Existing `.venv` – update dependencies:

```sh
.venv/bin/uv pip install -p .venv -r requirements_dev.txt
```

From scratch (needs any `uv`, e.g. `pip install uv` in a throwaway venv):

```sh
uv venv --python 3.14 .venv
uv pip install -p .venv -r requirements_dev.txt
```

The `homeassistant` wheel is ~55 MB. On a slow or flaky connection, set
`UV_HTTP_TIMEOUT=30 UV_HTTP_RETRIES=5`.

## Smoke test

```sh
.venv/bin/python scripts/smoke_test.py
```

Starts the simulator on port 15020, enables every module (energy manager, 3 heat pumps, 5 boilers,
5 buffers, 2 solar, 12 heat circuits) and reads everything once with `LambdaModbusHub`, for both
`latest_firmware=False` and `True`. Expected output:

```
latest_firmware=False: 260 values OK
latest_firmware=True: 290 values OK
```

An exception or `AssertionError` means the hub is broken. Run it after every change.

## Simulator

```sh
.venv/bin/python scripts/simulator.py              # 127.0.0.1:5020
.venv/bin/python scripts/simulator.py --host 0.0.0.0 --port 5020
```

Modbus TCP server, device ID 1, holding registers 0–6299. Every register returns `215`, which decodes
to 21.5 (÷10) or 2.15 (÷100). Operating states are therefore shown as the raw number, not as text.

To use it with a Home Assistant instance, add the Lambda integration with host `127.0.0.1` (or the
machine running the simulator) and port `5020`. Use `--host 0.0.0.0` if HA runs in Docker or on
another machine.

Change `REGISTER_VALUE` in `simulator.py` for other values. Per-register values are not supported yet.
