# 트리 지름 찾기 - 첫 노드에서 가장 먼 노드 탐색 / 1번에 의해 선정된 노드기준 가장 먼 노트 탐색
import sys
from collections import deque
m = sys.stdin.readline

number = int(m())
node = [[] for _ in range(number+1)]

for _ in range(number-1):
    a, b, distance = map(int, m().split())
    node[a].append([b, distance])
    node[b].append([a, distance])

def search(item):
    visited = [0] * (number + 1)
    a, b = 0, 0
    start = deque(node[item])
    visited[item] = 1
    while start:
        to, dis = start.popleft()
        visited[to] = 1
         
        if b < dis:
            a, b = to, dis
            
        for next_to, next_dis in node[to]:
            if visited[next_to] == 0:
                start.append([next_to, dis + next_dis])
                
    return [a, b]
tmp = search(1)
print(search(tmp[0])[1])
