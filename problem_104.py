# Even or Odd Checker: Write a Python function called `even_or_odd` that takes an integer as input and returns “Even” if the number is even and “Odd” if the number is odd. Test the function with different numbers.
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(4))   # Even
print(even_or_odd(7))   # Odd
print(even_or_odd(0))   # Even
print(even_or_odd(15))  # Odd
print(even_or_odd(-2))  # Even