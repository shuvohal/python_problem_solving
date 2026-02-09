#Tuple Sorting: Write a Python program to sort a tuple of integers in ascending order.
t = (5, 2, 9, 1, 7)

# Convert tuple to list, sort it, then convert back to tuple
sorted_tuple = tuple(sorted(t))

print("Sorted tuple:", sorted_tuple)
