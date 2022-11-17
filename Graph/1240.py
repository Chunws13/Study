# 1240
import sys, heapq
m = sys.stdin.readline

node, need = map(int, m().split())
info = {}

for _ in range(node-1):
    f, t, d = map(int, m().split())
    if f not in info:
        info[f] = [[t, d]]
    
    elif t not in info[f]:
        info[f].append([t,d])
    
    if t not in info:
        info[t] = [[f, d]]
    
    elif f not in info[t]:
        info[t].append([f, d])

find_distance = [list(map(int, m().split())) for _ in range(need)]
answer = []

for i, j in find_distance:
    visited = [0] * (node + 1)
    start = info[i][:]
    while start:
        s, d = heapq.heappop(start)
        visited[s] = 1
        if s == j:
            answer.append(d)
            break
        
        for next, next_dis in info[s]:
            if visited[next] == 1:
                continue
            visited[next] = 1
            heapq.heappush(start, [next, d + next_dis])
        
for a in answer:
    print(a)
