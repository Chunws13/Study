import sys
import heapq
m = sys.stdin.readline

jew, pack = map(int, m().split())
j_info = sorted([list(map(int, m().split())) for _ in range(jew)])
pack_info = sorted([int(m()) for _ in range(pack)], reverse=True)

answer, result = [], 0
while pack_info:
    p = pack_info.pop()
    while j_info and j_info[0][0] <= p:
        w, v = heapq.heappop(j_info)
        heapq.heappush(answer, -v)
    
    if answer:
        result -= heapq.heappop(answer)

print(result)
