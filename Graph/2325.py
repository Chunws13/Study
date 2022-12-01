# 2325
import sys, heapq, math
input = sys.stdin.readline

point, road = map(int, input().split())
info = [[] for _ in range(point+1)]
origin = [[0] *(point +1) for _ in range(point+1)]

for _ in range(road):
    a, b, c = map(int, input().split())
    info[a].append([b, c])
    info[b].append([a, c])
    
    origin[a][b] = c
    origin[b][a] = c

inf = math.inf
answer = [inf] * (point + 1)

def find_way():
    start = [[0, 1]]
    answer[1] = 0
    while start:
        cost, now = heapq.heappop(start)
        if answer[now] < cost:
            continue
        
        for next, n_cost in info[now]:
            next_cost = n_cost + cost
            if answer[next] > next_cost:
                answer[next] = next_cost
                heapq.heappush(start, [next_cost, next])

def track():
    start = [point]
    ways = []
    while start:
        s = start.pop()
        if s == 1:
            break
        
        for pre, cost in info[s]:
            if answer[pre] + cost == answer[s]:
                ways.append([pre, s])
                start.append(pre)
    
    return ways

find_way()
short_route = track()

result = 0
for from_, to_ in short_route:
    visited = [[0] * (point+1) for _ in range(point+1)]
    visited[from_][to_], visited[to_][from_] = 1, 1
    
    answer = [inf] * (point + 1)
    start = [[0, 1]]
    
    while start:
        cost, now = heapq.heappop(start)
        if answer[now] < cost:
            continue
        
        for next, n_cost in info[now]:
            next_cost = n_cost + cost
            if visited[next][now] or visited[now][next]:
                continue
            
            if answer[next] > next_cost:
                answer[next] = next_cost
                heapq.heappush(start, [next_cost, next])

        
    result = max(result, answer[-1])

print(result)
