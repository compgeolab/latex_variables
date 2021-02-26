"""
Convert Python variable to LaTeX variable
-----------------------------------------
"""
import latex_variables as lv

# Define a height in meters
height = 30

# Convert the variable into a LaTeX variable
variable = lv.to_latex(height, name="Height", unit="m", fmt="5g")
print(variable)
