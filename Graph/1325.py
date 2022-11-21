import sys
from collections import deque
input = sys.stdin.readline

com, node = map(int, input().split())
info = [[] for _ in range(com + 1)]

for _ in range(node):
    a, b = map(int, input().split())
    info[b] += [a]

answer = []
max_num = 0
for i in range(1, com + 1):
    start = deque([i])
    visited = [0] * len(info)
    visited[i] = 1
    tmp = 0
    
    while start:
        s = start.popleft()
        tmp += 1
        for j in info[s]:
            if visited[j] == 0:
                visited[j] = 1
                start.append(j)
    
    if tmp > max_num:
        answer = [i]
        max_num = tmp
    
    elif tmp == max_num:
        answer.append(i)
    
answer.sort()
for a in answer:
    print(a, end = ' ')
