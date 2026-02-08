#List Reversal: Write a Python program to reverse a given list without using any built-in functions.
numbers = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])
print("The reversed list is:", reversed_list)