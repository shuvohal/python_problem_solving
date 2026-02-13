'''
Task
The provided code stub reads two integers,a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,a // b.
The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.
Input Format
The first line contains the first integer, a. The second line contains the second integer, b.
Constraints

1 <= a <= 10^10
1 <= b <= 10^10
Output Format
Print the result of integer division, a // b, on the first line. Print the result of float division, a / b, on the second line.
Sample Input 0
4
3
Sample Output 0
1
1.3333333333333333
Explanation 0
The result of integer division is 1, while the result of float division is 1.3333333333333333.

'''
a = int(input().strip())
b = int(input().strip())
print(a // b)  # Integer division
print(a / b)   # Float division

