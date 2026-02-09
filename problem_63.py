#Matrix Transpose: Write a Python program to transpose a given matrix represented as a nested list.
# Given matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transpose matrix
transpose = []

for j in range(len(matrix[0])):      # columns
    row = []
    for i in range(len(matrix)):     # rows
        row.append(matrix[i][j])
    transpose.append(row)

# Print transposed matrix
print("Transposed Matrix:")
for r in transpose:
    print(r)
