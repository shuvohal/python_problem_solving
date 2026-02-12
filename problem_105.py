#List Sum Calculator: Write a Python function called `list_sum` that takes a list of integers as input and returns the sum of all elements in the list. Test the function with different lists.
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# Test the list_sum function with different lists
print(list_sum([1, 2, 3, 4, 5]))  # Output: 15
print(list_sum([-1, 0, 1]))        # Output: 0  
print(list_sum([]))               # Output: 0
print(list_sum([10, 20, 30]))     # Output: 60
print(list_sum([5, 5, 5, 5]))     # Output: 20
