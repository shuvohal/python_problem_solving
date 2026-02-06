#Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.
'''
A quadratic equation is of the form: ax^2 + bx + c = 0

The discriminant (d) is calculated as: d = b^2 - 4ac

x=-b±√b^2-4ac/2a
'''
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Two real roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)

elif d == 0:
    root = -b / (2*a)
    print("One real root:")
    print("Root:", root)

else:
    print("The roots are complex (no real roots).")
