#Print Patterns: Write a Python program using nested loops to print the following pattern:

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

'''
Outer loop (i) → controls the number of lines (1 to 5)
Inner loop (j) → prints the number of asterisks corresponding to the current line number (i)
The end="" argument in the print function prevents moving to a new line after printing each asterisk
After the inner loop completes, print() is called to move to the next line for the next iteration of the outer loop
''' 