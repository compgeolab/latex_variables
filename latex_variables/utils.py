"""
Utility functions
"""
import re


def build_latex_variable(name, value, unit):
    """
    Build string for defining a LaTeX variable

    Parameters
    ----------
    name : str
        Name of the LaTeX variable. Should be a valid name for a LaTeX
        variable (see `func:format_variable_name`).
    value : str
        String with the numbers for the LaTeX variable (see
        `func:format_value`).
    unit : str (optional)
        String for specifying the units (see `func:format_unit`).
    """
    check_latex_variable_name(name)
    if unit:
        return r"\newcommand{{\{name}}}{{${value} \, {unit}$}}".format(
            name=name, value=value, unit=unit
        )
    else:
        return r"\newcommand{{\{name}}}{{{value}}}".format(name=name, value=value)


def check_latex_variable_name(name):
    """
    Check if name for the LaTeX variable is valid
    """
    pattern = r"^[a-zA-Z]+$"
    if not re.match(name, pattern):
        raise ValueError("Invalid name for a LaTeX variable '{}'.".format(name))


def format_variable_name(name):
    """
    Convert Python variable name to a valid LaTeX variable name

    The conversion is carried out by removing underscores and
    capitalizing the first letter of each word.

    Example
    -------
    >>> _format_variable_name("my_variable")
    'MyVariable'
    """
    if len(name.split()) != 1:
        raise ValueError("Invalid variable name '{}'".format(name))
    return name.strip().replace("_", " ").title().replace(" ", "")


def format_value(value, fmt):
    """
    Convert numerical value to string with a specific format

    Parameters
    ----------
    value : int or float
        Numerical variable to convert.
    fmt : str
        String format used to apply the conversion

    Returns
    -------
    string_value : str
        String containing a formatted version of the value

    Examples
    --------
    >>> format_value(30.5, ".3f")
    '30.500'
    >>> format_value(30.5, "5g")
    '30.5'
    >>> format_value(123, "d")
    '123'
    >>> format_value(123, ".2f")
    '123.00'

    """
    return "{value:>{fmt}}".format(value=value, fmt=fmt).strip()


def format_unit(unit):
    """
    Format a string with units to LaTeX format

    Parameters
    ----------
    unit : str
        String containing units.
    """
    # Define regex pattern for units as alphabetic characters followed by
    # a positive or negative int.
    unit_pattern = r"^[a-zA-Z]+-?(\d+)?$"
    # Get each unit from the passed string
    splits = unit.strip().split()
    # Generate the LaTeX units
    units = []
    for split in splits:
        # Check if the passed unit has the valid format
        if not re.match(unit_pattern, split):
            raise ValueError("Invalid unit '{}'.".format(split))
        # Take the alphabetic characters of the unit and its power (if exists)
        alpha = re.findall("[a-zA-Z]+", split)[0]
        power = re.findall(r"-?\d+", split)
        # Build LaTeX unit
        unit_tex = r"\text{{{}}}".format(alpha)
        if power:
            unit_tex += "^{{{}}}".format(power[0])
        units.append(unit_tex)
    return r" ".join(units)
