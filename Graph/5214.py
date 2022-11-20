import sys
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().split())

info = [[] for _ in range(n + m + 1)]
for i in range(1, m + 1):
    hyper = list(map(int, input().split()))
    
    for h in hyper:
        info[h] += [n + i]
        info[n + i] += [h]

visited = [0] * (n + m + 1)
start = deque([[1, 1]])
visited[1] = 1
status = True

while start:
    s, d = start.popleft()
    if s == n:
        print(d // 2 + 1)
        status = False
        break
    
    for new_s in info[s]:
        if visited[new_s] == 0:
            visited[new_s] = 1
            start.append([new_s, d + 1])

if status:
    print(-1)
