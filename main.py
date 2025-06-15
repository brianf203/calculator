# Basic Python Calculator

# Ask the user for an expression
expression = input("Enter a mathematical expression: ")

# Split the expression into numbers and operator
parts = expression.split()

# Get the numbers and operator
num1 = float(parts[0])
operator = parts[1]
num2 = float(parts[2])

# Perform the calculation based on the operator

# Perform addition
if operator == "+":
    result = num1 + num2

# Perform subtraction
elif operator == "-":
    result = num1 - num2

# Perform multiplication
elif operator == "*":
    result = num1 * num2

# Perform division
elif operator == "/":
    result = num1 / num2

# Invalid operator
else:
    result = "Invalid operator"

# Print the result
print(f"The result is: {result}")
