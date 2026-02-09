#Dictionary Keys and Values: Write a Python program that takes a dictionary as input and prints all the keys and values in separate lines.
# Input dictionary
data = {
    "Name": "Alice",
    "Age": 20,
    "Marks": 85
}

print("Keys:")
for key in data.keys():
    print(key)

print("\nValues:")
for value in data.values():
    print(value)
