#Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles." )
else:
    print("The triangle is scalene.")

""" 
Equilateral: three equal sides

Isosceles: two equal sides

Scalene: all unequal sides
"""