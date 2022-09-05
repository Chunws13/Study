import sys
import math
m = sys.stdin.readline

a, b = map(int, m().split())
male = [0] + sorted(list(map(int, m().split())))
female = [0] + sorted(list(map(int, m().split())))

answer = [[0 for _ in range(b+1)] for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        if i == j:
            answer[i][j] = answer[i-1][j-1] + abs(male[i]-female[j])
        elif i > j:
            answer[i][j] = min(answer[i-1][j-1]+abs(male[i]-female[j]), answer[i-1][j])
        else:
            answer[i][j] = min(answer[i-1][j-1]+abs(male[i]-female[j]), answer[i][j-1])

print(answer[a][b])
