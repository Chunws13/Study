# 트리 부모 찾기
import sys
from collections import deque

m = sys.stdin.readline

number = int(m())

node = {}
for _ in range(number-1):
    a, b = map(int, m().split())
    node[a] = node.get(a, []) + [b]
    node[b] = node.get(b, []) + [a]

answer = [0] * (number + 1)

start = deque([1])
while start:
    s = start.popleft()
    for i in node[s]:
        if answer[i] == 0:
            answer[i] = s
            start.append(i)

for a in range(2, number + 1):
    print(answer[a])
            
