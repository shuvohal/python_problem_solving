#Sum of N numbers
#Take N then take N numbers → print total sum
N = int(input().strip())   # number of elements
total_sum = 0
for _ in range(N):
    num = int(input().strip()) 
    total_sum += num
print(total_sum)