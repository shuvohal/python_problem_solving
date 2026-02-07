#Print Patterns: Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on.
#Right-Angled Triangle
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
#Inverted Right-Angled Triangle
b=int(input("Enter number of rows: "))
for k in range(b, 0, -1):
    for z in range(k):
        print("*", end="")
    print()

#Right-Angled Triangle (Numbers)
c=int(input("Enter number of rows: "))
for d in range(1, c + 1):
    for l in range(1, d + 1):
        print(l, end="")
    print()

