# Dictionary Value Search: Given a dictionary of items and their prices, write a Python program to search for an item based on its price and print the item’s name.

# Dictionary of items and prices
items = {
    "Apple": 50,
    "Banana": 20,
    "Orange": 30,
    "Mango": 60
}

price = int(input("Enter price to search: "))

found = False

for item, item_price in items.items():
    if item_price == price:
        print("Item found:", item)
        found = True

if not found:
    print("No item found with that price")
