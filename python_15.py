#Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.
char = input("Enter a single character: ").lower()
vowels = "aeiou"
if char in vowels:
    print("It is a vowel.")
else:
    print("It is a consonant.")