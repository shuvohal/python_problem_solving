#Math Operations: Write a Python function called `math_operations` that takes three numbers and a string representing an operation (‘add’, ‘subtract’, ‘multiply’, or ‘divide’). The function should return the result of the specified operation on the three numbers. Implement the math operations as nested functions.
def math_operations(a, b, c, operation):

    def add():
        return a + b + c

    def subtract():
        return a - b - c

    def multiply():
        return a * b * c

    def divide():
        if b == 0 or c == 0:
            return "Cannot divide by zero"
        return a / b / c

    if operation == "add":
        return add()
    elif operation == "subtract":
        return subtract()
    elif operation == "multiply":
        return multiply()
    elif operation == "divide":
        return divide()
    else:
        return "Invalid operation"

# Test the math_operations function with different operations
print(math_operations(10, 5, 2, "add"))       # Output: 17
print(math_operations(10, 5, 2, "subtract"))  # Output: 3
print(math_operations(10, 5, 2, "multiply"))  # Output: 100
print(math_operations(10, 5, 2, "divide"))    # Output: 1.0
print(math_operations(10, 0, 2, "divide"))    # Output: Cannot divide by zero
print(math_operations(10, 5, 2, "modulus"))   # Output: Invalid operation