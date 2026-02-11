#Prime Number Checker: Write a Python program that takes a number as input and determines if it is a prime number or not. Use a `for` loop to check for factors. If a factor is found, `break` out of the loop.
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")

        #Only divisible by 1 and itself
