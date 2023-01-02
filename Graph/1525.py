# 1525
import sys, copy
from collections import deque
input = sys.stdin.readline

init_info = []
for _ in range(3):
    init_info += list(map(str, input().split()))

visited = {}
adr, adc = [1, -1, 0, 0], [0, 0, 1, -1]

start = deque([[init_info, 0]])

while start:
    now, calc = start.popleft()
    # print(now)
    if ''.join(now) == '123456780':
        print(calc)
        sys.exit()
    
    idx = now.index('0')
    row, col = idx // 3, idx % 3
    
    for k in range(4):
        new_r, new_c = row + adr[k], col + adc[k]
        if new_r < 0 or new_r >= 3 or new_c < 0 or new_c >= 3:
            continue
        
        n_idx = new_r * 3 + new_c
        next = list(now)
        next[idx], next[n_idx] = next[n_idx], next[idx]
                
        if visited.get(''.join(next)):
            continue
        
        visited[''.join(next)] = 1
        start.append([next, calc + 1])
        
print(-1)
