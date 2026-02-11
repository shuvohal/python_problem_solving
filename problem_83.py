# Dictionary Sorting: Given a dictionary with names as keys and corresponding ages as values, write a Python program to sort the dictionary based on age in ascending order.

# Dictionary with names and ages
data = {
    "Alice": 24,
    "Bob": 19,
    "Charlie": 22,
    "David": 21
}

# Sort by age (value)
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Sorted dictionary (by age):")
for name, age in sorted_data.items():
    print(name, ":", age)



