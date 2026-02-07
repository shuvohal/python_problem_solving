#Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.


n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
