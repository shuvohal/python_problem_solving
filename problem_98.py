#Odd Number Finder: Write a Python program to find the first odd number from a list of integers. Use a `for` loop and `break` to stop the loop when the first odd number is found.
numbers = [2, 4, 6, 8, 11, 14, 16]

for num in numbers:
    if num % 2 != 0:
        print("First odd number:", num)
        break
