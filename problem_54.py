#Tuple Reversal: Write a Python program to reverse a tuple without using any built-in functions.

t = (1, 2, 3, 4, 5)

reversed_tuple = ()
i = len(t) - 1

while i >= 0:
    reversed_tuple += (t[i],)
    i -= 1

print("Reversed tuple:", reversed_tuple)

