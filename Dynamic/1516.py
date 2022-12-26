# 1516
import sys, copy
from collections import deque
input = sys.stdin.readline

tower = int(input())
build_sequence = {t : [] for t in range(1, tower + 1)}
build_order = {}
build_time = {}

for t in range(1, tower + 1):
    build_info = list(map(int, input().split()))
    build_order[t] = 0
    for b in range(len(build_info)):
        if b == 0:
            build_time[t] = build_info[b]

        elif build_info[b] == -1:
            break
        
        else:
            build_sequence[build_info[b]].append(t)
            build_order[t] += 1

min_time = copy.deepcopy(build_time)
start = deque([])
for i in build_order:
    if build_order[i] == 0:
        start.append(i)

while start:
    s = start.popleft()
        
    for j in build_sequence[s]:
        build_order[j] -= 1
        min_time[j] = max(min_time[j], min_time[s] + build_time[j])
        if build_order[j] == 0:
            
            start.append(j)
    
for b in min_time:
    print(min_time[b])
