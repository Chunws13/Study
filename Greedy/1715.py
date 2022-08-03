# 카드 정리
import sys
import heapq
m = sys.stdin.readline

num = int(m())
pack = [int(m()) for i in range(num)]
heapq.heapify(pack)
answer = 0
while len(pack) > 1:
    one = heapq.heappop(pack)
    two = heapq.heappop(pack)
    
    answer = answer + one + two
    heapq.heappush(pack, one + two)
    
print(answer)
