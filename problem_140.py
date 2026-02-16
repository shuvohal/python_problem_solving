#Problem 3: Count Even Numbers

# Take N numbers and count how many are even
N = int(input().strip())
count = 0
for _ in range(N):
    num = int(input().strip())
    if num % 2 == 0:
        count += 1
print(count)