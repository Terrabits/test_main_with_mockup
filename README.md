# Test Main With Mockup

A project to demonstrate mockups for testing.

## Overview

This example project consists of the following parts:

### `Fsw` class

This project includes a class, [`Fsw`](project/fsw.py), which requires a TCP connection to an external resource.

### Executable Script `main.py`

This project includes an executable script: [`packages/main.py`](project/main.py).

This script imports  the `Fsw` class *at the module level*. Then, the imported `Fsw` class is used in the [`main`](project/main.py) script. Because it uses the Fsw class, `main` also requires a TCP connection to an external resource.

### Mock `Fsw`

For the purposes of testing, a [mock `Fsw`](project/mock/fsw.py) is also included. The mock `Fsw` does not require a TCP connection to an external resouerce. Instead, it provides a reasonable approximation of the behavior of `Fsw`.

### Inject Mocks into `main`

The mock `Fsw` is used in `tests/test_main.py`, since the developer and testing environments most likely do not contain the TCP connection to an external resource.

Furthermore, using a `mock` resource should speed up our tests considerably, which makes us much more likely to run them 😊.

#### Mock `Fsw` Module Injection

We note that there is a module-level variable, `main.Fsw`, created by calling `import`.

We also note that references to `Fsw` in the `main()` scope are actually references to the `main.Fsw` variable.

We can use this information to *inject* or replace `main.Fsw` with the mock `Fsw` before running our `main` test code.

```python
from project          import main  # main module
from project.mock.fsw import Fsw   # mock fsw
# ...


# use mock fsw for testing
main.Fsw = Fsw
```

See [`tests/test_main.py`](tests/test_main.py) for the complete test script.

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
