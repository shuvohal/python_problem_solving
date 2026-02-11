#Dictionary Key Removal: Given a dictionary of items and their quantities, write a Python program to remove a specific item from the dictionary based on user input.
# Dictionary of items and quantities
items = {
    "Apple": 10,
    "Banana": 20,
    "Orange": 15,
    "Mango": 8
}

key_to_remove = input("Enter item name to remove: ")

if key_to_remove in items:
    del items[key_to_remove]
    print("Item removed successfully.")
else:
    print("Item not found.")

print("Updated dictionary:", items)
