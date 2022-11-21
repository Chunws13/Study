# 1939
import sys
from collections import deque
input = sys.stdin.readline

n ,m = map(int, input().split())
bridge = [[] for _ in range(n+1)]
max_value, min_value = 0, 1000000000

for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append([b, c])
    bridge[b].append([a, c])
    max_value, min_value = max(max_value, c), min(min_value, c)

factory = list(map(int, input().split()))
result = 0

while min_value <= max_value:
    visited, start = set([factory[0]]), deque([factory[0]])
    mid = (max_value + min_value) // 2
    status = True
    
    while start:
        now = start.popleft()
        if now == factory[1]:
            status = False
            result = max(result, mid)
            break
        
        for next, n_weight in bridge[now]:
            if n_weight >= mid and next not in visited:
                visited.add(next)
                start.append(next)
        
    if status: # 도달 불가
        max_value = mid - 1
    
    else: # 도달 가능
        min_value = mid + 1
    
print(result)
