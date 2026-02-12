#Factorial Calculator: Write a Python function called `factorial` that takes an integer as input and returns its factorial. Test the function with different values.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result
# Test the factorial function with different values
print("Factorial of 5:", factorial(5))  # Output: 120
  
print("Factorial of 0:", factorial(0))  # Output: 1
print("Factorial of -3:", factorial(-3))  # Output: Factorial is not defined for negative numbers
