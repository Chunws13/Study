import sys
from collections import deque
m = sys.stdin.readline

info = deque(map(str, m().strip()))
boom = list(map(str, m().strip()))

answer = []
st = len(boom)
while info:
    i = info.popleft()
    answer.append(i)
    while answer and answer[-st:] == boom:
        k = 0
        while k < st:
            answer.pop()
            k += 1
    
if answer:
    print("".join(answer))

else:
    print("FRULA")
