#Problem 6: Count Words
#Take N lines (sentences) → count total words
N = int(input().strip())
total_words = 0
for _ in range(N):
    sentence = input().strip()
    words = sentence.split()
    total_words += len(words)
print(total_words)