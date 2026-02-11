#Nested Dictionary Key Search: Write a Python program that takes a key as input and searches for it in a nested dictionary. If found, print the corresponding value, otherwise, print “Key Not Found.”

# Nested dictionary
data = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "city": "Dhaka"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "city": "Chittagong"
    }
}

search_key = input("Enter key to search: ")

found = False

for outer_key in data:
    if search_key in data[outer_key]:
        print("Value:", data[outer_key][search_key])
        found = True
        break

if not found:
    print("Key Not Found")
