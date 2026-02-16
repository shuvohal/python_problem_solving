'''

Problem Statement:

Consider a list (list = []). You can perform the following commands:

insert i e → Insert integer e at position i

print → Print the list

remove e → Delete the first occurrence of integer e

append e → Insert integer e at the end of the list

sort → Sort the list

pop → Pop the last element from the list

reverse → Reverse the list

Task:

Initialize your list and read in the value of N, followed by N lines of commands.
For each command, perform the corresponding operation on the list in order.

Input Format

The first line contains an integer N, the number of commands

Each of the next N lines contains one of the commands listed above

Constraints

All inserted elements are integers

Output Format

For each command of type print, print the list on a new line

sample input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
sample output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
N = int(input().strip())   # number of commands
lst = []                   # empty list

for _ in range(N):        #Repeat the loop N times
    command = input().strip().split()

    if command[0] == "insert":
        i = int(command[1])
        e = int(command[2])
        lst.insert(i, e)

    elif command[0] == "print":
        print(lst)

    elif command[0] == "remove":
        e = int(command[1])
        lst.remove(e)

    elif command[0] == "append":
        e = int(command[1])
        lst.append(e)

    elif command[0] == "sort":
        lst.sort()

    elif command[0] == "pop":
        lst.pop()

    elif command[0] == "reverse":
        lst.reverse()
