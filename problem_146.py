'''
Problem 9: Mini Python List System

Commands:

add x

remove x

print
'''
N = int(input().strip())
my_list = []
for _ in range(N):
    command = input().strip().split()
    if command[0] == "add":
        x = int(command[1])
        my_list.append(x)
    elif command[0] == "remove":
        x = int(command[1])
        if x in my_list:
            my_list.remove(x)
    elif command[0] == "print":
        print(my_list)
