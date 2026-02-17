'''
Problem 15: Command Based Calculator

Commands:

add x

sub x

mul x

div x

print
'''
N = int(input().strip())
result = 0
for _ in range(N):
    command = input().strip().split()
    if command[0] == "add":
        x = int(command[1])
        result += x
    elif command[0] == "sub":
        x = int(command[1])
        result -= x
    elif command[0] == "mul":
        x = int(command[1])
        result *= x
    elif command[0] == "div":
        x = int(command[1])
        if x != 0:
            result //= x  # Using floor division for integer division
    elif command[0] == "print":
        print(result)

        
