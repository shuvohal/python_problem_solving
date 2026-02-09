#Nested List Sorting: Given a nested list containing lists of integers, write a Python program to sort the sublists based on their lengths.
nested_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]

# Sort sublists based on length
nested_list.sort(key=len)

print("Sorted nested list:", nested_list)
