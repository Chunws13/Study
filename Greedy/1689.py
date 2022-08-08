# 겹치는 선분 구하기

import sys
import heapq
m = sys.stdin.readline

count = int(m())
info = [list(map(int, m().split())) for _ in range(count)]
info.sort(reverse=True)

answer = 1
end_standard = []
while info:
    i = info.pop()
    while end_standard and end_standard[0] <= i[0]:
        heapq.heappop(end_standard)
    
    heapq.heappush(end_standard, i[1])
    answer = max(answer, len(end_standard))

print(answer)
