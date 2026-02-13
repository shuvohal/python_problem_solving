'''
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
Example
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
The ordered list of scores is [20.0, 50.0]. The second lowest score is 50.0. There are two students with that score: "beta" and "alpha". Ordered alphabetically, the names are printed as:
alpha 
beta
Input Format
The first line contains an integer, N, the number of students. The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.
Constraints
2 <= N <= 5
0 <= Grade <= 100
Output Format
Print the name(s) of any student(s) having the second lowest grade in alphabetical order, each on a new line.
Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.21
Akriti
41
Rohan
39
Sample Output 0
Berry
Harry
Tina
Explanation 0
There are 3 students with the lowest grade of 37.21, so we print their names in alphabetical order.
'''
# Read number of students
# Read number of students
N = int(input().strip())

students = []

# Take input for each student
for i in range(N):
    name = input().strip()
    grade = float(input().strip())
    students.append([name, grade])

# Get all unique grades and sort them
grades = sorted(set([student[1] for student in students]))

# Second lowest grade
second_lowest = grades[1]

# Get names of students with second lowest grade
names = [student[0] for student in students if student[1] == second_lowest]

# Sort names alphabetically
names.sort()

# Print each name in new line
for name in names:
    print(name)


