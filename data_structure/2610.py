# 2610
import sys, math
from collections import deque
input = sys.stdin.readline

num = int(input())
node = int(input())

info = [[] for _ in range(num + 1)]

for _ in range(node):
    a, b = map(int, input().split())
    info[a].append(b)
    info[b].append(a)

visited = [0] * (num + 1)
count = 1
stand = [] # 대표자

for i in range(1, num + 1):
    if visited[i]:
        continue
    
    start = deque([[i, count]])
    visited[i] = count
    group = [i]
    while start: # 그룹 형성
        n, cnt = start.popleft()
        
        for j in info[n]:
            if visited[j]:
                continue
            visited[j] = cnt
            start.append([j, cnt])
            group.append(j)
    
    min_time, tmp = math.inf, 0 # 전달 소요시간 / 임시 대표

    for g in group:
        time_table = [math.inf] * (num + 1)
        start = deque([[0, g]])
        
        # 개별 전달시간
        while start:
            t, s = start.popleft()
            
            if time_table[s] < t:
                continue
            
            time_table[s] = t
            for j in info[s]:
                start.append([t +1, j])

        # inf 제외
        tmp_time = 0
        for t in time_table:
            if t != math.inf:
                tmp_time = max(tmp_time, t)
        
        if tmp_time < min_time:
            min_time = tmp_time
            tmp = g
            
    stand.append(tmp)
    count += 1

print(max(visited))
for s in sorted(stand):
    print(s)
