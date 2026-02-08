#Matrix Multiplication: Write a Python program using nested loops to multiply two matrices.
# Define matrices
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Result matrix initialized with zeros
result = [
    [0, 0],
    [0, 0]
]

# Matrix multiplication using nested loops
for i in range(len(A)):          # rows of A
    for j in range(len(B[0])):   # columns of B
        for k in range(len(B)):  # rows of B
            result[i][j] += A[i][k] * B[k][j]

# Print result
print("Resultant Matrix:")
for row in result:
    print(row)
