#string Palindrome: Write a Python function to check if a given string is a palindrome or not.
# A palindrome is a string that reads the same backward as forward, ignoring spaces, punctuation, and capitalization.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage
print(is_palindrome("Madam"))        # True
print(is_palindrome("nurses run"))   # True
print(is_palindrome("Hello World"))  # False
print(is_palindrome("shuvo"))        # False
