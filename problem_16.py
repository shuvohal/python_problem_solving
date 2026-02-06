#. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.
time = int(input("Enter the time in hours (0-23): "))
if 0 <= time < 12:
    print("Good Morning")
elif 12 <= time < 18:
    print("Good Afternoon")
elif 18 <= time < 22:
    print("Good Evening")
elif 22 <= time < 24:
    print("Good Night")