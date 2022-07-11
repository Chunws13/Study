# 숨바꼭질 - 다익스트라 사용
import sys
import heapq
import math
m = sys.stdin.readline

bin, zin = map(int, m().split(' '))
INF = math.inf
move, t = [1, -1], [1, 1]
answer= [INF] * 100001
start = []
heapq.heappush(start,[0, bin])

while start:
    time, position = heapq.heappop(start)
    
    if answer[position] < time:
        continue
    
    if answer[position] > time:
        answer[position] = time
        
    for i in range(2):
        time_2, position_2 = time + t[i], position + move[i]
        if 0 <= position_2 <= len(answer)-1 and answer[position_2] > time_2:
            heapq.heappush(start, [time_2, position_2])
    
    if 0 <= position * 2 <= len(answer)-1 and answer[position * 2] > time:
            heapq.heappush(start, [time, position * 2])

print(answer[zin])
