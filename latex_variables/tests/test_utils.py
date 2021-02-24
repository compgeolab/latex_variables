"""
Test utility functions
"""
import pytest

from ..utils import format_unit


def test_format_unit():
    """
    Test format_unit function
    """
    units = [
        "m",
        "m2",
        "m-2",
        "kg",
        "kg2",
        "kg-4",
        "kg m-3",
        "kg2 m-5",
        "mGal",
        "J mGal-2",
    ]
    expected_outcomes = [
        r"\text{m}",
        r"\text{m}^{2}",
        r"\text{m}^{-2}",
        r"\text{kg}",
        r"\text{kg}^{2}",
        r"\text{kg}^{-4}",
        r"\text{kg} \, \text{m}^{-3}",
        r"\text{kg}^{2} \, \text{m}^{-5}",
        r"\text{mGal}",
        r"\text{J} \, \text{mGal}^{-2}",
    ]
    for unit, expected in zip(units, expected_outcomes):
        assert format_unit(unit) == expected


def test_format_unit_invalid():
    """
    Test format_unit with invalid inputs
    """
    with pytest.raises(ValueError):
        format_unit("2m")
    with pytest.raises(ValueError):
        format_unit("m2kg")
    with pytest.raises(ValueError):
        format_unit("m-kg")
