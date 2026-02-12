#Greatest Common Divisor (GCD) Calculator: Write a Python function called `gcd` that takes two integers as input and returns their greatest common divisor. Test the function with different pairs of numbers.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# Test the gcd function with different pairs of numbers
print(gcd(48, 18))  # Output: 6
print(gcd(56, 98))  # Output: 14
print(gcd(101, 10)) # Output: 1
print(gcd(54, 24))  # Output: 6
print(gcd(0, 5))     # Output: 5
print(gcd(5, 0))     # Output: 5
