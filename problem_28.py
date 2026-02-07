#List Manipulation: Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.
numbers = [10, 20, 30, 40, 50]

total = 0
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    total += num

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
#List (তালিকা) হলো এমন একটি ডেটা স্ট্রাকচার যা একাধিক মান সংরক্ষণ করতে পারে এবং প্রতিটি মান একটি নির্দিষ্ট অবস্থানে থাকে।