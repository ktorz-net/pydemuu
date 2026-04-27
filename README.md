# PyDemuu - Demuu Python Library

It is mainly a Python wrapper of the _libDemuu_ elements.
_PyDemuu_ also introduces some user-friendly Python classes to better manage _Demuu_ concepts.

## Install

**Attention:** Actually, only `x86` machin under `Linux` OS are supported.

The _pyDemuu_ package does not rely on any dependencies.
Installation is performed with _pip_ after cloning this repository:

```sh
git clone git@github.com:ktorz-net/pydemuu.git
pip install ./pydemuu
```

The 'example-421.py' file provides a simple example for _demuu_ inspired by the _421_ game. The command `python3 example-421.py` should instantiate a model for _421_ and test _2_ transitions. 

## Test

_pyDemuu_ is developed according to the test-driven method based with the `pytest` framework.

```sh
pip install pytest
pytest
```
