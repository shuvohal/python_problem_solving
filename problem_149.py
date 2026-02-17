'''
Problem 12: Frequency Counter

Input N numbers
print how many times each number appears
'''
N = int(input().strip())
frequency = {}
for _ in range(N):
    num = int(input().strip())
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for num, count in frequency.items():
    print(f"{num} appears {count} times")
    