import sys
import heapq
m = sys.stdin.readline

problem = int(m())
info = [list(map(int, m().split())) for _ in range(problem)]

info.sort(reverse=True)
answer = []

while info:
    i = info.pop()
    heapq.heappush(answer, i[1])
    if len(answer) > i[0] :
        heapq.heappop(answer)
        

print(sum(answer))
