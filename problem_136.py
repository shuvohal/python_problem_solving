#Practice Problem 6: Top 3 Students
'''
Print names of Top 3 highest scoring students
'''
N = int(input().strip())

students = []

for i in range(N):
    name = input().strip()
    marks = float(input().strip())
    students.append([name, marks])

# Sort by marks descending
students.sort(key=lambda x: x[1], reverse=True)

top3 = students[:3]

# Sort top3 names alphabetically
names = [s[0] for s in top3]
names.sort()

for name in names:
    print(name)

