#Problem 5: Simple List Append
#ake N commands, each line append x → print final list
N = int(input().strip())
my_list = []
for _ in range(N):
    command = input().strip().split()
    if command[0] == "append":
        x = int(command[1])
        my_list.append(x)
print(my_list)