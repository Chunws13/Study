#9251
import sys
m = sys.stdin.readline

a = [' '] + list(map(str, m().strip()))
b = [' '] + list(map(str, m().strip()))

answer = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            answer[i][j] = answer[i-1][j-1] + 1
        else:
            answer[i][j] = max(answer[i-1][j], answer[i][j-1])
print(answer[-1][-1])
