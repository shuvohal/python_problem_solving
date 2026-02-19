'''
ছয়টি ক্রমিক সংখ্যার প্রথম তিনটির যোগফল 30 হলে শেষ তিনটির যোগফল কত?
'''
# given sum of first three numbers
first_sum = 30

# 3x + 3 = first_sum
x = (first_sum - 3) // 3

# create 6 consecutive numbers
numbers = [x, x+1, x+2, x+3, x+4, x+5]

# calculate last 3 numbers sum
last_sum = numbers[3] + numbers[4] + numbers[5]

print("Six numbers:", numbers)
print("Last three sum =", last_sum)
