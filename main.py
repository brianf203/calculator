# Function for addition
def add(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for division
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

# Main calculator function
def calculator(expression):
    # Split the expression into numbers and operator
    parts = expression.split()

    # Get the numbers and operator
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    # Perform the calculation based on the operator
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        return "Invalid operator"

# Ask the user for an expression
expression = input("Enter a mathematical expression (e.g., 3 + 4): ")

# Get and print the result
result = calculator(expression)
print(f"The result is: {result}")
