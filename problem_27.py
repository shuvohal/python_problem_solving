#Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

n=int(input())
i=2
while i<n:
    if n%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")
#Prime number (প্রাইম সংখ্যা) হলো এমন একটি ধনাত্মক পূর্ণসংখ্যা যা কেবলমাত্র ১ এবং নিজেকে দিয়ে বিভাজ্য।
a = int(input())

for j in range(2, a):
    if a % j == 0:
        print("Not Prime")
        break
else:
    print("Prime")
