'''
Problem 11: Second Largest Number

Input N numbers
print second largest

'''
N = int(input().strip())
max_num = float('-inf')  # Initialize to negative infinity
second_max = float('-inf')
for _ in range(N):
    num = int(input().strip())
    if num > max_num:
        second_max = max_num  # Update second max before updating max
        max_num = num
    elif second_max < num < max_num:  # Update second max if it's between current second max and max
        second_max = num
print(second_max)