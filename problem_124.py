#Task: Input an email and print username part before @.
email = input("Enter an email address: ")
username = email.split('@')[0]
print(username)

'''
split() means: break a string into parts based on a delimiter (like space, comma, or @) and return a list of those parts.

# single integer
n = int(input().strip())

# multiple integers
a, b = map(int, input().split())

# list of integers
nums = list(map(int, input().split()))

# string input
s = input().strip()

# multiple lines
lines = [input().strip() for _ in range(3)]

'''

text = "I love Python"

words = text.split()

print(words)
