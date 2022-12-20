# 5582
import sys
input = sys.stdin.readline

c = list(map(str, input().strip()))
r = list(map(str, input().strip()))

info = [[0] * (len(c) + 1) for _ in range(len(r) + 1)]

for i in range(len(r)):
    for j in range(len(c)):
        if c[j] == r[i]:
            info[i+1][j+1] = info[i][j] + 1

print(max(map(max, info)))
