"""
.. _overview:

Overview
========

The ``latex_variables`` package provides functions to convert any numerical
Python variable to a string that defines a LaTeX variable, which can be
included in your LaTeX document.
This avoids the need to manually type the value of the variable into the
document and opens the potential to automatically update its value when the
Python code that generates it is changed.

The library
-----------

Most functions are available through the :mod:`latex_variables` top level
package. Throughout the documentation we'll use ``lv`` as the alias for
:mod:`latex_variables`.

"""
import latex_variables as lv

###############################################################################
# .. _convert_variable:
#
# Convert variables
# -----------------
#
# We can use the :func:`latex_variables.to_latex` to generate the string needed
# to define a LaTeX variable with the same value as the Python variable and
# optional units.
#
# Let's define some height measurement in meters and generate its corresponding
# LaTeX variable. We need to pass a ``name`` for it and because this magntiude
# has a known unit, we will also pass a value to the ``unit`` argument.

height = 30
variable = lv.to_latex(height, name="Height", unit="m")
print(variable)

###############################################################################
# Python floats might have many significant digits that are not needed to
# report on a LaTeX document, while a round version of it it's sufficient to
# achieve the same purpose. We can specify the format of the numerical value of
# the variable through the ``fmt`` argument.

pressure = 101.325
variable = lv.to_latex(pressure, name="Pressure", unit="kPa", fmt=".2f")
print(variable)
