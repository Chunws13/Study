# 2589
import sys, copy
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
info = [list(map(str, input().strip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]
land = []
for i in range(r):
    for j in range(c):
        if info[i][j] == 'W':
            visited[i][j] = 1

        if info[i][j] == 'L':
            land.append([i, j])

result = 0
for row, col in land:
    start = deque([[row, col, 0]])
    new_visited = copy.deepcopy(visited)
    new_visited[row][col] = 1
    while start:
        ro, co, mo = start.popleft()
        
        for k in range(4):
            new_r, new_c = ad_r[k] + ro, ad_c[k] + co
            if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c or new_visited[new_r][new_c]:
                continue
            
            new_visited[new_r][new_c] = mo + 1
            start.append([new_r, new_c, mo + 1])
    
    result = max(result, max(map(max, new_visited)))

print(result)
