"""Core HalfRand sequence generation APIs."""

from __future__ import annotations

import random
import warnings
from dataclasses import dataclass, field
from typing import Iterator


@dataclass(slots=True)
class HalfRandom:
    """A stateful generator whose values vary by a bounded random step.

    Args:
        step: Maximum absolute change between adjacent values.
        seed: Optional seed used by an isolated pseudo-random generator.
        lower: Optional inclusive lower bound. Values are clipped to it.
        upper: Optional inclusive upper bound. Values are clipped to it.

    ``HalfRandom`` does not modify Python's module-level random state.
    """

    step: float = 0.1
    seed: int | str | bytes | bytearray | float | None = None
    lower: float | None = None
    upper: float | None = None
    _random: random.Random = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if self.step < 0:
            raise ValueError("step must be greater than or equal to zero")
        if self.lower is not None and self.upper is not None and self.lower > self.upper:
            raise ValueError("lower must be less than or equal to upper")
        self._random = random.Random(self.seed)

    def generate(self, count: int, *, start: float | None = None) -> list[float]:
        """Return ``count`` values, optionally beginning at ``start``.

        Without a start value, the first value is sampled uniformly from the
        configured bounds, or from ``[0, 1]`` when bounds are omitted.
        """

        if isinstance(count, bool) or not isinstance(count, int):
            raise TypeError("count must be an integer")
        if count < 0:
            raise ValueError("count must be greater than or equal to zero")
        if count == 0:
            return []

        current = self._initial_value() if start is None else self._clip(float(start))
        values = [current]
        for _ in range(count - 1):
            current = self._clip(current + self._random.uniform(-self.step, self.step))
            values.append(current)
        return values

    def iter(self, *, start: float | None = None) -> Iterator[float]:
        """Yield an infinite sequence, beginning at ``start`` when provided."""

        current = self._initial_value() if start is None else self._clip(float(start))
        while True:
            yield current
            current = self._clip(current + self._random.uniform(-self.step, self.step))

    def _initial_value(self) -> float:
        lower = 0.0 if self.lower is None else self.lower
        upper = 1.0 if self.upper is None else self.upper
        return self._random.uniform(lower, upper)

    def _clip(self, value: float) -> float:
        if self.lower is not None:
            value = max(self.lower, value)
        if self.upper is not None:
            value = min(self.upper, value)
        return value


def generate(
    count: int,
    *,
    step: float = 0.1,
    seed: int | str | bytes | bytearray | float | None = None,
    start: float | None = None,
    lower: float | None = None,
    upper: float | None = None,
) -> list[float]:
    """Generate a smoothly varying pseudo-random sequence.

    This convenience function creates a new :class:`HalfRandom` instance for
    each call. Pass a seed for reproducible output.
    """

    return HalfRandom(step=step, seed=seed, lower=lower, upper=upper).generate(
        count, start=start
    )


def randomNum(n: int) -> list[float]:  # noqa: N802 - retained compatibility
    """Return ``n`` values using the legacy API (deprecated)."""

    warnings.warn(
        "randomNum() is deprecated; use halfrand.generate() instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return generate(n)
