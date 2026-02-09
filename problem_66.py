#Maximum Element in Nested List: Write a Python program to find the maximum element in a nested list of integers.
nested_list = [[3, 7, 2], [9, 1, 5], [4, 8, 6]]

max_value = nested_list[0][0]

for sublist in nested_list:
    for num in sublist:
        if num > max_value:
            max_value = num

print("Maximum element:", max_value)

