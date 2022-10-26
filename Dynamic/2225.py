# 2225
import sys
m = sys.stdin.readline

t, n = map(int, m().split())
info = list([i for i in range(t+1)])

answer = [[0] * (t+1) for _ in range(n+1)]
answer[0][0] = 1

for i in range(1, n+1):
    for j in range(t+1):
        answer[i][j] = answer[i-1][j] + answer[i][j-1]

print(answer[-1][-1]%1000000000)
