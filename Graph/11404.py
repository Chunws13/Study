# 플로이드 - 플로이드_와샬
import sys
import math
m = sys.stdin.readline

city = int(m())
bus_num = int(m())

answer = [[INF] * (city + 1) for _ in range(city + 1)]
INF = math.inf
for _ in range(bus_num):
    f, t, cost = map(int, m().split(' '))
    answer[f][t] = min(answer[f][t], cost)

for i in range(len(answer)):
    for j in range(len(answer)):
        if i == j:
            answer[i][j] = 0

for i in range(1, len(answer)):
    for j in range(1, len(answer)):
        for k in range(1, len(answer)):
            answer[j][k] = min(answer[j][k], answer[j][i] + answer[i][k])

for a in range(1, len(answer)):
    for b in range(1, len(answer)):
        if answer[a][b] == INF:
            print(0, end= ' ')
        else:
            print(answer[a][b], end = ' ')
        
    print()
