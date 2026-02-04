#String Reverse: Write a Python function to reverse a given string and return the reversed string.
def reverse_string(s):
    return s[::-1]
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

