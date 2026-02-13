#Task: Input numbers as string and convert to integer list.
numbers_str = input("Enter numbers separated by space: ")
numbers_list = list(map(int, numbers_str.split()))
print(numbers_list)