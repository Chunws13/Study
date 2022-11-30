# 13334
import sys, heapq
input = sys.stdin.readline

people = int(input())
info = []

for _ in range(people):
    a, b = map(int, input().split())
    info.append([min(a, b), max(a, b)])
    
road = int(input())

info.sort(key=lambda x:x[1], reverse=True)

answer = 0
que = []
while info:
    i = info.pop()
    l = i[1] - i[0]
    if l > road:
        continue
    
    while que and que[0] < i[1] - road:
        heapq.heappop(que)    
    
    heapq.heappush(que, i[0])
    answer = max(answer, len(que))
    
print(answer)
