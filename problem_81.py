#Dictionary Merging: Given two dictionaries, write a Python program to merge them into a single dictionary and print the result.
dict1 = {
    "A": 10,
    "B": 20
}

dict2 = {
    "C": 30,
    "D": 40
}

# Merge dictionaries
merged_dict = dict1 | dict2

print("Merged Dictionary:", merged_dict)
