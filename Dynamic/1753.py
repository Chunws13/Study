# 최단경로 - 다익스트라
import sys
import heapq
import math
m = sys.stdin.readline

number, count = map(int, m().split(' '))
zero = int(m())
INF = math.inf

answer = [INF] * (number + 1)
road = [[] for i in range(number + 1)]

for c in range(count):
    f, t, v = map(int, m().split(' '))
    road[f].append((v, t))

start = []
heapq.heappush(start, (0, zero))

while start:
    s = heapq.heappop(start)

    value, to = s[0], s[1]
    if answer[to] < value:
        continue
    
    for r2 in road[to]:
        value_1, to_1 = r2[0]+value, r2[1]
    
        if answer[to_1] > value_1:
            answer[to_1] = value_1
            heapq.heappush(start, (value_1, to_1))

for a in range(1, number + 1):
    if a == zero:
        print(0)
    elif answer[a] == INF:
        print("INF")
    else:
        print(answer[a])
