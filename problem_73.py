#Set Symmetric Difference: Given two sets A and B, write a Python program to find the symmetric difference between the two sets (i.e., elements that are present in either set A or set B, but not in both) and print the result.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

symmetric_diff = A.symmetric_difference(B)

print("Symmetric difference:", symmetric_diff)
