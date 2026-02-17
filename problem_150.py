'''
Problem 13: Gym Member System (your project related)

Commands:
add name
remove name
print

manage member list
'''
N = int(input().strip())
my_list = []
for _ in range(N):
    command = input().strip().split()
    if command[0] == "add":
        name = command[1]
        my_list.append(name)
    elif command[0] == "remove":
        name = command[1]
        if name in my_list:
            my_list.remove(name)
    elif command[0] == "print":
        print(my_list)
        