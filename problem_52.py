#Tuple Frequency Count: Given a tuple containing various elements, write a Python program to count the frequency of a specific element in the tuple.
t = (1, 2, 3, 2, 4, 2, 5)
element = int(input("Enter element to count: "))

count = 0

for item in t:
    if item == element:
        count += 1

print("Frequency of", element, ":", count)
