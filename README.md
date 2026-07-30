<div align="center">

# 〰️ HalfRand

**Small, reproducible pseudo-random sequences with smooth, bounded changes.**

[![CI](https://github.com/KageRyo/HalfRand/actions/workflows/ci.yml/badge.svg)](https://github.com/KageRyo/HalfRand/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

HalfRand is a lightweight Python library for producing random-walk-like data. The first
value is sampled randomly (or supplied by you), then each following value changes by no
more than a configurable step. It is useful for demos, mock time series, simulations,
animations, and tests that need natural-looking variation.

> [!NOTE]
> HalfRand produces pseudo-random data and is **not suitable for cryptography, security,
> gambling, or scientific sampling that requires independent observations**.

## ✨ Features

- Dependency-free library core built on the Python standard library
- Reproducible results with local, isolated seeded generators
- One-shot, stateful, and infinite-iterator APIs
- Optional lower and upper bounds
- CSV command-line interface
- Type hints, tests, packaging metadata, and CI

## 📦 Installation

Install the latest release when it is available on PyPI:

```bash
python -m pip install halfrand
```

Or install the current GitHub version:

```bash
python -m pip install "git+https://github.com/KageRyo/HalfRand.git"
```

For local development, see [CONTRIBUTING.md](CONTRIBUTING.md).

## 🚀 Quick start

### Convenience API

```python
from halfrand import generate

values = generate(8, seed=42, step=0.05)
print(values)
```

The same seed and arguments produce the same values:

```python
assert generate(8, seed=42) == generate(8, seed=42)
```

### Bounds and starting value

```python
temperatures = generate(
    24,
    seed=7,
    start=20.0,
    step=0.8,
    lower=15.0,
    upper=30.0,
)
```

Bounds use clipping: a step that crosses a boundary lands exactly on that boundary.

### Stateful and streaming APIs

```python
from itertools import islice
from halfrand import HalfRandom

generator = HalfRandom(seed=42, step=0.1)
first_batch = generator.generate(5)
second_batch = generator.generate(5)  # continues consuming the generator's random state

stream = HalfRandom(seed=42).iter(start=0.5)
first_ten = list(islice(stream, 10))
```

## 🖥️ Command line

Installing the package provides a `halfrand` command. It writes CSV to standard output:

```bash
halfrand 5 --seed 42
```

Write a larger bounded sequence to a file:

```bash
halfrand 100 --seed 42 --step 0.05 --lower 0 --upper 1 --output values.csv
```

Run `halfrand --help` for all options. The legacy `python main.py` entry point remains
available and delegates to the same CLI.

## 🧠 How it works

Given the current value `x` and maximum step `s`, HalfRand samples `d` uniformly from
`[-s, s]` and computes the next value as `x + d`. Configured bounds then clip the value:

```text
x₀ = supplied start, or Uniform(lower, upper)
xₙ = clip(xₙ₋₁ + Uniform(-step, step), lower, upper)
```

Adjacent values are correlated. The word “half” describes this balance between random
movement and continuity; it is not a formal statistical term.

## 📚 API reference

### `generate(count, *, step=0.1, seed=None, start=None, lower=None, upper=None)`

Returns a `list[float]`. `count` must be a non-negative integer, `step` must be
non-negative, and `lower` cannot exceed `upper`. An empty count returns an empty list.

### `HalfRandom(step=0.1, seed=None, lower=None, upper=None)`

A reusable generator with `generate(count, *, start=None)` and `iter(*, start=None)`
methods. Each instance owns its random state and does not modify `random`'s global state.

### Compatibility

The original `randomNum(n)` function is temporarily available but deprecated. New code
should use `generate(n)`.

## 🤝 Community and support

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
- Use [GitHub Issues](https://github.com/KageRyo/HalfRand/issues) for reproducible bugs and feature proposals.
- Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).
- Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).

## 🏷️ Versioning and releases

HalfRand follows [Semantic Versioning](https://semver.org/). The initial library release
is `0.1.0`: its public API is usable, but the `0.x` series leaves room to refine that API
before committing to `1.0.0` compatibility guarantees. Maintainers can follow the
[release checklist](CONTRIBUTING.md#releasing); pushing a matching `v*` tag triggers the
automated PyPI and GitHub release workflow.

## 📄 License

HalfRand is available under the [MIT License](LICENSE).

<div align="center">Made with ❤️ for the open-source community.</div>
