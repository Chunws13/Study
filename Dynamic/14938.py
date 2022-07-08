# 서강그라운드 - 다익스트라
import sys
import heapq
m = sys.stdin.readline

ground, talent, road = map(int, m().split(' '))
item = [0] + list(map(int, m().split(' ')))
info = [[] for _ in range(ground + 1)]
answer = [0] * (ground + 1)

for _ in range(road):
    f, to, distance = map(int, m().split(' '))
    info[f].append([distance, to])
    info[to].append([distance, f])

visited = []
for g in range(1, ground + 1):
    start = []
    heapq.heappush(start, [0, g])
    
    while start:
        dis, target = heapq.heappop(start)
        
        if dis > talent:
            continue
        
        if target not in visited:
            visited.append(target)
            answer[g] += item[target]
        
        for d, t in info[target]:
            if d + dis <= talent:
                heapq.heappush(start, [d+dis, t])
    visited = []
print(max(answer))
