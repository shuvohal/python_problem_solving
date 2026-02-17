'''
Problem 14: Product Cart System

Commands:

add price

remove price

total

print

like ecommerce cart (useful for your Fiverr gig related to ecommerce)
'''
N = int(input().strip())
cart = []
for _ in range(N):
    command = input().strip().split()
    if command[0] == "add":
        price = float(command[1])
        cart.append(price)
    elif command[0] == "remove":
        price = float(command[1])
        if price in cart:
            cart.remove(price)
    elif command[0] == "total":
        print(sum(cart))
    elif command[0] == "print":
        print(cart)
        