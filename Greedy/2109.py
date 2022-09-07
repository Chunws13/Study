import sys
import heapq
m = sys.stdin.readline

num = int(m())
info = [list(map(int, m().split())) for _ in range(num)]
info.sort(key=lambda x:x[1], reverse=True)

answer = []
while info:
    i = info.pop()
    heapq.heappush(answer, i[0])
    if len(answer) > i[1]:
        heapq.heappop(answer)
    
print(sum(answer))
