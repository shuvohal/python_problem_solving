# List Manipulation: Given two lists of integers, write a Python program to create a new list that contains elements common to both lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []
for num in list1:
    if num in list2:
        common_elements.append(num)
print("The common elements in both lists are:", common_elements)
