#Duplicate Removal: Write a Python program that takes a list of elements as input and creates a new set containing only the unique elements from the list.
elements = input("Enter elements separated by space: ").split()

unique_elements = set(elements)

print("Unique elements:", unique_elements)
