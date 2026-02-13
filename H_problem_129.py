'''
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up. 
Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Constraints
2 <= n <= 10
-100 <= A[i] <= 100
Output Format
Print the runner-up score.
Sample Input 0
5
2 3 6 6 5
Sample Output 0
5
Explanation 0
Given the list of scores [2, 3, 6, 6, 5], the maximum score is 6. The runner-up score is the second highest score, which is 5.

'''
# Read input
n = int(input().strip())
arr = list(map(int, input().split()))

# Remove duplicates by converting to set
unique_scores = list(set(arr))

# Sort the list in descending order
unique_scores.sort(reverse=True)

# Runner-up score = second element
print(unique_scores[1])
