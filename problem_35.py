#List Average: Write a Python program to calculate the average of all elements in a given list of integers.
numbers = [1, 2, 3, 4, 5]
total_sum = 0
for num in numbers:
    total_sum += num
average = total_sum / len(numbers)
print("The average of the list is:", average)