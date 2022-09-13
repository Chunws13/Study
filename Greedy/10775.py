import sys
from collections import deque
m = sys.stdin.readline

gates = int(m())
airplanes = int(m())
info = deque([int(m()) for _ in range(airplanes)])

answer = [0] * (gates + 1)
result = 0
while info:
    i = info.popleft()
    while i and answer[i]:
        answer[i] += 1
        i -= (answer[i] - 1)
        
    if i <= 0:
        break
    else:
        answer[i] = 1
        result += 1
        
print(result)
