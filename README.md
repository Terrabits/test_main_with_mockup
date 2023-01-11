# Test Main With Mockup

This project includes a class, [`Fsw`](project/fsw.py), which requires a TCP connection to an external resource.

The `Fsw` class is then used in the [`main`](project/main.py) script, which requires this TCP connection to an external resource.

For the purposes of testing, a [mock `Fsw`](project/mock/fsw.py) is also included. This mockup is used in `tests/test_main.py` to avoid the external resource requirement.

## Requirements

In general, this project requires the following:

- Python 3+
- python package `rohdeschwarz`

Specifically, this project was tested with `CPython 3.11` and the exact packages and versions listed in [`requirements-win64.txt.lock`](./requirements-win64.txt.lock).

## Install

Run [scripts\install.bat](scripts/install.bat) to install packages from `requirements-win64.txt.lock`.

## Run Main Script

Execute [scripts\start.bat](scripts/start.bat) to run [`project/main.py`](project/main.py). Note that this script attempts to connect to an Fsw at TCPIP address `localhost`. Edit this address to reflect the actual `Fsw` address.

## Tests

Run [scripts\test.bat](scripts/test.bat) to run all tests located in [tests/](./tests). This includes [tests/test_main.py], which is "monkeypatched" to use the mock `Fsw` class.
