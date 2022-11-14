# 1915
import sys
m = sys.stdin.readline

r, c = map(int, m().split())
info = [[0] * (c+1)]

for _ in range(r):
    info.append([0] + list(map(int, m().strip())))

answer = [[0] * (c+1) for _ in range(r+1)]

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if info[i][j] == 0:
            continue
        answer[i][j] = min(answer[i-1][j], answer[i][j-1], answer[i-1][j-1]) + 1

result = max(map(max, answer))
print(result * result)
