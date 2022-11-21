# 10282
import sys, heapq
from collections import deque
input = sys.stdin.readline

case = int(input())
result = []
for _ in range(case):
    com, node, init_com = map(int, input().split())
    info = [[] for _ in range(com+1)]
    
    for _ in range(node):
        a, b, c = map(int, input().split())
        info[b].append([a, c])
    
    start = [[0, init_com]]
    visited = [0] * (com + 1)
    tmp, max_time = 0, 0
    
    while start:
        t, c = heapq.heappop(start)
        if visited[c] == 0:
            tmp += 1
            visited[c] = 1
            max_time = max(t, max_time)
        
            for next, tim in info[c]:
                if visited[next] == 0:
                    heapq.heappush(start, [tim + t,  next])

    result.append([tmp, max_time])

for r, t in result:
    print(r, t)
