#Word Palindrome Checker: Write a Python program that takes a word as input and checks if it is a palindrome (reads the same forwards and backward). Use `continue` to skip checking the word if its length is less than 3 characters.
while True:
    word = input("Enter a word: ")

    if len(word) < 3:
        print("Word must be at least 3 characters long.")
        continue

    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

    break

#A palindrome is a word, number, or phrase that reads the same forward and backward.
