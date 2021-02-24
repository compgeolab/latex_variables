"""
Convert variables to LaTeX variable definitions
"""
from varname import nameof

from .utils import (
    build_latex_variable,
    format_variable_name,
    format_value,
    format_unit,
    check_latex_variable_name,
)


def to_latex(variable, name=None, unit=None, fmt=None):
    """
    Converts a variable to a LaTeX variable definition

    Parameters
    ----------
    variable : float or int
        Variable to convert to a LaTeX variable definition.
    name : str (optional)
        Variable name for the LaTeX variable. If None, the name of ``variable``
        will be used after small formatting for a valid LaTeX variable. Default
        to None.
    unit : str (optional)
        Units of the variable. Default to None.
    fmt : str (optional)
        Format to use for printing the variable. If None, no formatting will be
        done, the variable will be shown with full precision. Default to None.

    Returns
    -------
    latex_variable : str
        String used to define a LaTeX variable.

    Example
    -------
    >>> height = 30
    >>> unit = "m"
    >>> to_latex(height, unit="m")
    r'\\newcommand{\\Height}{$30 \\, \\text{m}$}'

    >>> density = 2670
    >>> unit = "kg m-3"
    >>> to_latex(height, unit="m")
    r'\\newcommand{\\Height}{$2670 \\, \\text{kg} \\text{m}^{-3}$}'

    """
    # Create LaTeX variable name from Python variable name if `name` is None
    if name is None:
        name = format_variable_name(nameof(variable))
    # Format value of the variable
    if fmt:
        value = format_value(variable, fmt)
    else:
        value = str(variable)
    # Format unit for LaTeX variable definition string
    if unit:
        unit = format_unit(unit)
    return build_latex_variable(name, value, unit)
