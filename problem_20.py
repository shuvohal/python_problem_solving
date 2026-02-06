#Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.
n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum of first", n, "natural numbers is:", total)
