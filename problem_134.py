#Practice Problem 4: Students Above Average
'''
Print names of students whose marks are above average.
'''
N = int(input().strip())

students = []

for i in range(N):
    name = input().strip()
    marks = float(input().strip())
    students.append([name, marks])

avg = sum([s[1] for s in students]) / N

names = [s[0] for s in students if s[1] > avg]

names.sort()

for name in names:
    print(name)
