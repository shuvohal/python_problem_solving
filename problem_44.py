# Matrix Addition: Write a Python program to add two matrices represented as nested lists.
# Define two matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

# Result matrix initialized with zeros
result = [
    [0, 0, 0],
    [0, 0, 0]
]

# Matrix addition using nested loops
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

# Print result
print("Resultant Matrix:")
for row in result:
    print(row)
