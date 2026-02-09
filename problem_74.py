#Set Operations: Given three sets A, B, and C, write a Python program to find and print the intersection of A and B, the union of B and C, and the difference between C and A.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {4, 6, 7, 8}

# Intersection of A and B
intersection_AB = A & B

# Union of B and C
union_BC = B | C

# Difference between C and A
difference_CA = C - A

print("Intersection of A and B:", intersection_AB)
print("Union of B and C:", union_BC)
print("Difference between C and A:", difference_CA)
