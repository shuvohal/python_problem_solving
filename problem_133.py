#Practice Problem 3: Average Marks

'''
Find and print average marks of all students.

'''

N = int(input().strip())

students = []

for i in range(N):
    name = input().strip()
    marks = float(input().strip())
    students.append([name, marks])

total = sum([s[1] for s in students])

average = total / N

print(round(average, 2))
