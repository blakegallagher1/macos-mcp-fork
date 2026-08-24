"""Utility math functions for the Oh My Pi project.

Extended to support Python's :class:`decimal.Decimal` and :class:`fractions.Fraction`
numeric types in addition to the built‑in ``int`` and ``float``.
"""

from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from typing import Union

Number = Union[int, float, Decimal, Fraction]


def multiply(a: Number, b: Number) -> Number:
    """Return the product of *a* and *b*.

    Supported types are ``int``, ``float``, ``Decimal`` and ``Fraction``.
    Types are not coerced – the operation uses Python's native ``*`` which
    preserves the more precise type (e.g. ``Decimal`` * ``Decimal`` yields a
    ``Decimal``). A ``TypeError`` is raised for unsupported types.
    """
    if not isinstance(a, (int, float, Decimal, Fraction)):
        raise TypeError(f"multiply expects numeric types, got {type(a)!r}")
    if not isinstance(b, (int, float, Decimal, Fraction)):
        raise TypeError(f"multiply expects numeric types, got {type(b)!r}")
    return a * b
