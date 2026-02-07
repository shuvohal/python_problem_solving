#Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
n = int(input("Enter the limit: "))

a, b = 0, 1
print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Fibonacci sequence হলো এমন একটি সংখ্যা ধারা যেখানে প্রতিটি সংখ্যা আগের দুইটি সংখ্যার যোগফল।