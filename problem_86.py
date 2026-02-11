# Dictionary Key Check: Write a Python program that takes a key as input and checks if it exists in a given dictionary. Print “Key Found” if the key is present and “Key Not Found” otherwise.
data = {
    "Name": "Alice",
    "Age": 20,
    "City": "Dhaka"
}

key = input("Enter key to search: ")

if key in data:
    print("Key Found")
else:
    print("Key Not Found")
