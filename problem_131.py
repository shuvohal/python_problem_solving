#Practice Problem 1: Highest Score Students
'''
Take N students (name + marks).
Print the names of students who got the highest marks in alphabetical order.
'''
N = int(input().strip())

students = []

for i in range(N):
    name = input().strip()
    marks = float(input().strip())
    students.append([name, marks])

# Find highest marks
max_marks = max([s[1] for s in students])

# Get students with highest marks
names = [s[0] for s in students if s[1] == max_marks]

# Sort alphabetically
names.sort()

# Print
for name in names:
    print(name)

