import sys
from collections import deque
m = sys.stdin.readline

total, d = map(int, m().split())
info = deque(map(int, m().strip()))
target = total - d
answer = []
while info:
    i = info.popleft()
    while answer and d > 0:
        if answer[-1] < i:
            answer.pop()
            d -= 1
        else:
            break
    answer.append(i)

while len(answer) > target:
    answer.pop()

print(''.join(map(str, answer)))
