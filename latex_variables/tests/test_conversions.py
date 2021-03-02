"""
Test conversions
"""
from ..conversions import to_latex


def test_conversion_to_latex():
    """
    Test expected behaviour of to_latex() function
    """
    my_variable = 3.1416
    my_other_variable = 3.141592653589793
    my_length = 5400
    my_area = 200
    my_density = 2670

    assert (
        to_latex(my_variable, name="MyVariable") == r"\newcommand{\MyVariable}{3.1416}"
    )
    assert to_latex(my_variable, name="Pi") == r"\newcommand{\Pi}{3.1416}"
    assert (
        to_latex(my_variable, name="MyVariable", fmt=".3f")
        == r"\newcommand{\MyVariable}{3.142}"
    )
    assert (
        to_latex(my_other_variable, name="MyOtherVariable")
        == r"\newcommand{\MyOtherVariable}{3.141592653589793}"
    )
    assert (
        to_latex(my_other_variable, name="MyOtherVariable", fmt=".4f")
        == r"\newcommand{\MyOtherVariable}{3.1416}"
    )
    assert (
        to_latex(my_length, name="MyLength", unit="m")
        == r"\newcommand{\MyLength}{$5400 \, \text{m}$}"
    )
    assert (
        to_latex(my_area, name="MyArea", unit="m2")
        == r"\newcommand{\MyArea}{$200 \, \text{m}^{2}$}"
    )
    assert (
        to_latex(my_density, name="MyDensity", unit="kg m-3")
        == r"\newcommand{\MyDensity}{$2670 \, \text{kg} \text{m}^{-3}$}"
    )
