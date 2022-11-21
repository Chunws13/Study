# 5719
import sys, heapq, math
from collections import deque

input = sys.stdin.readline
inf = math.inf

result = []

def find_route():
    route = [[0, start]]
    distance[start] = 0
    
    while route:
        dis, now = heapq.heappop(route)
        if distance[now] < dis:
            continue
    
        for next, next_time in info[now]:
            if visited[now][next] == 1:
                continue
            
            if distance[next] > dis + next_time:
                distance[next] = dis + next_time
                heapq.heappush(route, [dis + next_time, next])

def route_check():
    que = deque()
    que.append(end)
    while que:
        now = que.popleft()
        if now == start:
            continue
        
        for pre, dis in reverse_info[now]:
            if visited[pre][now]:
                continue
            
            if distance[now] == distance[pre] + dis:
                visited[pre][now] = 1
                que.append(pre)

while True:
    location, road = map(int, input().split())
    
    if location == 0 and road == 0:
        break
    
    start, end = map(int, input().split())
    info, reverse_info = [[] for _ in range(location + 1)], [[] for _ in range(location + 1)]
    
    for _ in range(road):
        a, b, c = map(int, input().split())
        info[a].append([b, c])
        reverse_info[b].append([a, c])
        
    visited = [[0] * (location + 1) for _ in range(location + 1)]
    distance = [inf] * (location + 1)
    find_route()
    
    route_check()
    
    distance = [inf] * (location + 1)
    find_route()
    
    if distance[end] != inf:
        result.append(distance[end])
    
    else:
        result.append(-1)
        
for r in result:
    print(r)
