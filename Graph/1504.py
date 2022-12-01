# 1504
import sys, heapq, math
input = sys.stdin.readline

n, e = map(int, input().split())
info = [[] for _ in range(n+1)]

inf = math.inf
answer = [[inf] * (n+1) for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    info[a].append([b, c])
    info[b].append([a, c])

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            answer[i][j] = 0

route_a, route_b = map(int, input().split())

for i in [1, route_a, route_b]:
    start = [[0, i]]
    answer[i][i] = 0
    while start:
        cost, now = heapq.heappop(start)
        if answer[i][now] < cost:
            continue
        
        for next, n_cost in info[now]:
            next_cost = n_cost + cost
            if next_cost < answer[i][next]:
                answer[i][next] = next_cost
                heapq.heappush(start, [next_cost, next])

result = min(answer[1][route_a] + answer[route_a][route_b] + answer[route_b][n],
             answer[1][route_b] + answer[route_b][route_a] + answer[route_a][n])

if result == inf:
    print(-1)
    
else:
    print(result)
