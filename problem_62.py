#List of Tuples Conversion: Given a nested list containing tuples of (x, y) coordinates, write a Python program to convert it into a list of x-coordinates and a list of y-coordinates.
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

x_coords = []
y_coords = []

for x, y in points:
    x_coords.append(x)
    y_coords.append(y)

print("X-coordinates:", x_coords)
print("Y-coordinates:", y_coords)

