#Tuple Operations: Given two tuples of integers, write a Python program to perform element-wise addition, subtraction, and multiplication and create new tuples for each operation.
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

add_tuple = ()
sub_tuple = ()
mul_tuple = ()

for i in range(len(t1)):
    add_tuple += (t1[i] + t2[i],)
    sub_tuple += (t1[i] - t2[i],)
    mul_tuple += (t1[i] * t2[i],)

print("Addition tuple:", add_tuple)
print("Subtraction tuple:", sub_tuple)
print("Multiplication tuple:", mul_tuple)
