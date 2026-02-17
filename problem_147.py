'''
Problem 10: Student Grade System

Input N students
Each line: name marks
Print student with highest marks
'''
N = int(input().strip())
students = []
for _ in range(N):
    name = input().strip()
    marks = float(input().strip())
    students.append((name, marks))
# Sort by marks descending
students.sort(key=lambda x: x[1], reverse=True)
# Get top student
top_student = students[0]
print(top_student[0])
