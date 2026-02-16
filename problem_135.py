#Practice Problem 5: Pass / Fail System
'''
If marks ≥ 40 → Pass
Else → Fail

'''
N = int(input().strip())

for i in range(N):
    name = input().strip()
    marks = float(input().strip())

    if marks >= 40:
        print(name, "Pass")
    else:
        print(name, "Fail")
