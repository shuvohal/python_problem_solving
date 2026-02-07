#Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.
n = int(input("Enter a number: "))

sum_even = 0
i = 2

while i <= n:
    sum_even += i
    i += 2

print("Sum of even numbers between 1 and", n, "is:", sum_even)


#Even numbers (জোড় সংখ্যা) হলো এমন সংখ্যা যা ২ দ্বারা বিভাজ্য হয়, যেমন ২, ৪, ৬, ইত্যাদি।