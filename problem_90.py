# Nested Dictionary Sorting: Given a nested dictionary containing product details (product name, price, and quantity), write a Python program to sort the products based on their prices in ascending order.
# Nested dictionary of products
products = {
    "P1": {"name": "Laptop", "price": 80000, "quantity": 5},
    "P2": {"name": "Mobile", "price": 30000, "quantity": 10},
    "P3": {"name": "Tablet", "price": 40000, "quantity": 7}
}

# Sort products by price
sorted_products = dict(
    sorted(products.items(), key=lambda item: item[1]["price"])
)

print("Products sorted by price (ascending):")
for product_id, details in sorted_products.items():
    print(product_id, ":", details)
