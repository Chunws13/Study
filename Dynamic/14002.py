#14002
import sys
from unittest import result
m = sys.stdin.readline

size = int(m())
info = list(map(int, m().split()))
answer = [1] * size
result = []
for i in range(size):
    for j in range(i):
        if info[i] > info[j]:
            answer[i] = max(answer[j] + 1, answer[i])

idx = max(answer)
index = answer.index(idx)
result.append(info[index])
for i in range(index, -1, -1):
    if result[-1] > info[i] and answer[i] == idx-1:
        idx -= 1
        result.append(info[i])

print(max(answer))
print(" ".join(map(str, result[::-1])))
