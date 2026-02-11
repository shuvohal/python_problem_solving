# Nested Dictionary Length: Write a Python program to calculate and print the total number of key-value pairs in a nested dictionary.

students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "address": "Dhaka"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "address": "Chittagong"
    }
}

total_pairs = 0

for key in students:
    total_pairs += len(students[key])

print("Total number of key-value pairs:", total_pairs)
