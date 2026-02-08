
# List Max and Min: Write a Python program to find the maximum and minimum values in a given list of integers.
numbers = [3, 1, 4, 1, 5, 9]
max_value = numbers[0]  
min_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("The maximum value in the list is:", max_value)
print("The minimum value in the list is:", min_value)
