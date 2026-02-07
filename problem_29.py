#Reverse String: Write a Python program using a while loop to reverse a given string.Nested Loops:

s = input("Enter a string: ")

rev = ""
i = len(s) - 1

while i >= 0:
    rev += s[i]
    i -= 1

print("Reversed string:", rev)

'''
Takes a string as input

Starts from the last index of the string

Adds each character to rev

Moves backward using while

Prints the reversed string
'''