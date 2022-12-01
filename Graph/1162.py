# 11404
import sys, heapq, math
input = sys.stdin.readline

city, road, need = map(int, input().split())
info = [ [] for _ in range(city + 1)]

for _ in range(road):
    a, b, c = map(int, input().split())
    info[a].append([b, c])
    info[b].append([a, c])

inf = math.inf
start = [[0, 0, 1]]
answer = [[inf] * (need + 1) for _ in range(city+1)]
answer[1][0] = 0

while start:
    cost, chance, now = heapq.heappop(start)
    if answer[now][chance] < cost:
        continue
    
    for next, n_cost in info[now]:
        if n_cost + cost < answer[next][chance]:
            heapq.heappush(start, [cost + n_cost, chance, next])
            answer[next][chance] = n_cost + cost
            
        if chance < need and cost < answer[next][chance+1]:
            heapq.heappush(start, [cost, chance+1, next])
            answer[next][chance+1] = cost
    
print(min(answer[-1]))
