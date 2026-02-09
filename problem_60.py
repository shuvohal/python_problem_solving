#Nested List Flattening: Write a Python program to flatten a nested list and convert it into a single-dimensional list.


nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print("Flattened list:", flat_list)
