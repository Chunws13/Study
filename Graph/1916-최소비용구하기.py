import sys, math, heapq
m = sys.stdin.readline

city, bus = int(m()), int(m())
bus_route = [[] for _ in range(city + 1)]
min_cost = [math.inf] * (city + 1)

for _ in range(bus):
    frm, to, cost = map(int, m().split(' '))
    
    bus_route[frm].append([to, cost])

start, end = map(int,m().split(' '))

now = []
heapq.heappush(now, [0, start])

# dfs 구현 시 시간 초과
# 배열의 첫번째 요소가 최소값을 보장하도록 heapq 사용
while now :
    v, n = heapq.heappop(now)
    if n == end:
        print(v)
        break
    
    for i in bus_route[n]:
        next_n, next_v = i[0],  i[1] + v

        if min_cost[next_n] > next_v:
            min_cost[next_n] = next_v
            heapq.heappush(now, [next_v, next_n])
