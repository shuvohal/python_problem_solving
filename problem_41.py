# List Element Count: Write a Python program to count the occurrences of a specific element in a given list.
numbers = [1, 2, 3, 2, 4, 2, 5]
element = int(input("Enter element to count: "))

count = 0

for num in numbers:
    if num == element:
        count += 1

print("Occurrences of", element, ":", count)
