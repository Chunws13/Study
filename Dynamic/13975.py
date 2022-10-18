import sys
import heapq
m = sys.stdin.readline
case = int(m())
answer = []
for _ in range(case):
    size = int(m())
    info = list(map(int, m().split()))
    heapq.heapify(info)
    tmp = 0
    
    while len(info) != 1:
        a, b  = heapq.heappop(info), heapq.heappop(info)
        heapq.heappush(info, a+b)
        tmp += a + b
    answer.append(tmp)

for a in answer:
    print(a)
