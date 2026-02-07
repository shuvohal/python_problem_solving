#Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.
n = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print("Factorial of", n, "is:", factorial)

 #Factorial (ফ্যাক্টোরিয়াল) হলো কোনো সংখ্যার ১ থেকে ঐ সংখ্যা পর্যন্ত সব ধনাত্মক সংখ্যার গুণফল।