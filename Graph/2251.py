# 2251
import sys, copy
from collections import deque
input = sys.stdin.readline

max_a, max_b, max_c = map(int, input().split())
status = [[[0] * (max_c + 1) for _ in range(max_b + 1)] for _ in range(max_a + 1)]
max_info = [max_a, max_b, max_c]

answer = []
start = deque([[0, 0, max_c]])
status[0][0][max_c] = 1

while start:
    bottle = start.popleft()

    if bottle[0] == 0 and bottle[2] not in answer:
        answer.append(bottle[2])
    
    for i in range(3):
        if bottle[i] == 0:
            continue
        
        for j in range(1, 3):
            new_bottle = copy.deepcopy(bottle)
            idx = (i + j) % 3
            new_bottle[i], new_bottle[idx] = max(new_bottle[i] - max_info[idx] + new_bottle[idx], 0), min(new_bottle[i] + new_bottle[idx], max_info[idx])
            
            if status[new_bottle[0]][new_bottle[1]][new_bottle[2]]:
                continue
            
            status[new_bottle[0]][new_bottle[1]][new_bottle[2]] = 1
            start.append([new_bottle[0], new_bottle[1], new_bottle[2]])

print(' '.join(map(str, sorted(answer))))
