'''
Task

Given an integer n and n space-separated integers as input:

Create a tuple t of those integers

Then compute and print the result of hash(t)

🔹 Input Format

First line contains an integer n (number of elements)

Second line contains n space-separated integers describing the tuple elements

🔹 Output Format

Print the result of hash(t)
Sample Input
2
1 2
Sample Output
3713081631934410656

'''
n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))
