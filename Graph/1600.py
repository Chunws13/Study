# 1600
import sys
input = sys.stdin.readline
from collections import deque

chance = int(input())
c, r = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(r)]
visited = [[[0] * (chance + 1) for _ in range(c)] for _ in range(r)]

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]
chance_r, chance_c = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]

start = deque([[0, 0, 0, 0]])
visited[0][0][0] = 1
answer = -1
while start:
    row, col, move, ch = start.popleft()
    
    if row == r - 1 and col == c -1:
        answer = move
        break
    
    for i in range(4):
        new_r, new_c = ad_r[i] + row, ad_c[i] + col
        if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c or info[new_r][new_c]:
            continue
        
        if visited[new_r][new_c][ch]:
            continue
        
        visited[new_r][new_c][ch] = 1
        start.append([new_r, new_c, move + 1, ch])
    
    if ch < chance:
        for j in range(8):
            new_r, new_c = chance_r[j] + row, chance_c[j] + col
            if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c or info[new_r][new_c]:
                continue
            
            if visited[new_r][new_c][ch+1]:
                continue
            
            visited[new_r][new_c][ch+1] = 1
            start.append([new_r, new_c, move + 1, ch+1])

print(answer)
