# List Element Frequency: Given a nested list containing lists of integers, write a Python program to count the frequency of each element in the entire nested list.
nested_list = [[1, 2, 3], [2, 3, 4], [1, 2, 5]]

frequency = {}

for sublist in nested_list:
    for item in sublist:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

print("Element Frequency:")
for key, value in frequency.items():
    print(key, ":", value)
