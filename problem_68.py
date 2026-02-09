# Nested List Element Search: Write a Python program to search for a specific element in a nested list and return its position (row and column indices).
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = int(input("Enter element to search: "))

found = False

for i in range(len(matrix)):          # rows
    for j in range(len(matrix[i])):   # columns
        if matrix[i][j] == target:
            print("Element found at row:", i, "column:", j)
            found = True
            break
    if found:
        break

if not found:
    print("Element not found")
