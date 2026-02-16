#Practice Problem 2: Third Lowest Score
'''
Print students who got the 3rd lowest marks.
'''
N = int(input().strip())

students = []

for i in range(N):
    name = input().strip()
    marks = float(input().strip())
    students.append([name, marks])

# Unique sorted marks
marks_list = sorted(set([s[1] for s in students]))

third_lowest = marks_list[2]

names = [s[0] for s in students if s[1] == third_lowest]

names.sort()

for name in names:
    print(name)
