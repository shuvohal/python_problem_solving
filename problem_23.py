#Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.

n = int(input("Enter an integer: "))

count = 0
num = abs(n)   # handle negative numbers

while num > 0:
    count += 1
    num //= 10

print("Number of digits:", count)

'''
num //= 10 মানে—

num কে ১০ দিয়ে ভাগ করা

দশমিক বাদ দেওয়া

শেষ অঙ্কটি কেটে ফেলা
'''
