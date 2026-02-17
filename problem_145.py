#Problem 8: Find Max Number
#Take N numbers and find the maximum
N = int(input().strip())
max_num = float('-inf')  # Initialize to negative infinity
for _ in range(N):
    num = int(input().strip())
    if num > max_num:
        max_num = num
print(max_num)