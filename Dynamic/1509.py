import sys, math
input = sys.stdin.readline

word = [''] + list(map(str, input().strip()))
table = [[0] * len(word) for _ in range(len(word))]

INF = math.inf
answer = [INF] * len(word)

answer[0], answer[1] = 0, 1
for i in range(1, len(word)):
    table[i][i] = 1
    
    if i < len(word)-1 and word[i] == word[i+1]:
        table[i][i+1] = 1

for i in range(len(word) - 2, -1, -1):
    for j in range(len(word) - 1, i + 1, -1):
        if word[i] == word[j] and table[i+1][j-1]:
            table[i][j] = 1

for end in range(1, len(word)):
    for start in range(1, end):
        if table[start][end]:
            answer[end] = min(answer[end], answer[start-1] + 1)
            
        else:
            answer[end] = min(answer[end], answer[end-1] + 1)
        
print(answer[-1])
