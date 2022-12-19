# 1245
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c = map(int, input().split())
mountain  = [list(map(int, input().split())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

ad_r, ad_c = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
result = 0

def check(i, j):
    global status
    visited[i][j] = 1
    
    for k in range(8):
        new_r, new_c = i + ad_r[k], j + ad_c[k]
        
        if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
            continue
        
        if mountain[new_r][new_c] > mountain[i][j]:
            status = False
        
        if mountain[new_r][new_c] == mountain[i][j] and visited[new_r][new_c] == 0:
            check(new_r, new_c)

for i in range(r):
    for j in range(c):
        if mountain[i][j] > 0 and visited[i][j] == 0:
            status = True
            check(i, j)
            if status:
                result += 1

print(result)
