# 17142
import sys, math, copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

size, v = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(size)]

v_info = []
for r in range(size):
    for c in range(size):
        if info[r][c] == 2:
            v_info.append([r, c, 0])
            info[r][c] = '*'
        
        if info[r][c] == 1:
            info[r][c] = '-'
        
        if info[r][c] == 0:
            info[r][c] = -1
            
ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]
virus = list(combinations(v_info, v))
inf = math.inf
result = []

for v in virus:
    answer = 0
    start = deque(v)
    board = copy.deepcopy(info)
    
    visited = [[0] * size for _ in range(size)]
    
    while start:
        row, col, time = start.popleft()
        
        visited[row][col] = 1
        board[row][col] = time
        
        for i in range(4):
            new_r, new_c = row + ad_r[i], col + ad_c[i]
            
            if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:
                continue
            
            if visited[new_r][new_c] or board[new_r][new_c] != -1:
                continue
            
            visited[new_r][new_c] = 1
            start.append([new_r, new_c, time + 1])
    
    status = False
    for i in range(size):
        for j in range(size):
            if board[i][j] == -1:
                status = True
                break
            
            try:
                answer = max(answer, int(board[i][j]))
            
            except:
                pass
    
    if status:
        result.append(inf)
    
    else:
        result.append(answer)
result.sort()
if result[0] == inf:
    print(-1)
else:
    print(result)
