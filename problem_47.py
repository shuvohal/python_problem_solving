#Transpose Matrix: Write a Python program to transpose a given matrix represented as a nested list.
# Original matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transposed matrix
transpose = []

for j in range(len(matrix[0])):      # columns
    row = []
    for i in range(len(matrix)):     # rows
        row.append(matrix[i][j])
    transpose.append(row)

# Print result
print("Transposed Matrix:")
for r in transpose:
    print(r)
