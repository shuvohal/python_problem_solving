# Multiplication Table: Write a Python program using nested loops to print the multiplication table from 1 to 10.
for i in range(1, 11):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()   # blank line between tables
'''
Outer loop (i) → selects the table number (1 to 10)

Inner loop (j) → multiplies i by numbers from 1 to 10

Prints a blank line after each table for readability
'''