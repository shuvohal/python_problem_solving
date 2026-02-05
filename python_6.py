#Data Type Checker: Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).
def check_data_type(variable):
    return type(variable).__name__

# Example usage:
example_var = 42
print(check_data_type(example_var))  # Output: int

example_var = 3.14
print(check_data_type(example_var))  # Output: float

example_var = "Hello"
print(check_data_type(example_var))  # Output: str

example_var = [1, 2, 3]
print(check_data_type(example_var))  # Output: list