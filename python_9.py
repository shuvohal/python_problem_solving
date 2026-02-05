#String Concatenation: Write a Python program that takes two strings as input and concatenates them into a single string without using the `+` operator.
def concatenate_strings(str1, str2):
    return " ".join([str1, str2])

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

print("Concatenated string:", concatenate_strings(string1, string2))
