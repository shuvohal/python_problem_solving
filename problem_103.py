#Palindrome Checker: Write a Python function called `is_palindrome` that takes a string as input and returns `True` if it is a palindrome and `False` otherwise. Test the function with different words.
def is_palindrome(text):
    text = text.lower()   # Make case-insensitive
    return text == text[::-1]
print(is_palindrome("madam"))    # True
print(is_palindrome("level"))    # True
print(is_palindrome("hello"))    # False
print(is_palindrome("Radar"))    # True
print(is_palindrome("Python"))   # False
