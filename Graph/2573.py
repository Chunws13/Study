# 2573
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(r)]
ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

def melt():
    melt_point = []
    for i in range(r):
        for j in range(c):
            if info[i][j] == 0:
                
                for k in range(4):
                    new_r, new_c = ad_r[k] + i, ad_c[k] + j
                    if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
                        continue
                    
                    if info[new_r][new_c] > 0:
                        melt_point.append([new_r, new_c])
                    
    return melt_point

result = 1
while True:
    visited = [[0] * c for _ in range(r)]
    
    melting = melt()
    for row, col in melting:
        info[row][col] = max(info[row][col]- 1, 0)
    
    count = 0
    for i in range(r):
        for j in range(c):
            if visited[i][j] == 0 and info[i][j] > 0:
                count += 1
                start = [[i, j]]
                visited[i][j] = 1
                while start:
                    row, col = start.pop()
                    
                    for k in range(4):
                        new_r, new_c = ad_r[k] + row, ad_c[k] + col
                    
                        if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c or visited[new_r][new_c]:
                            continue
                        
                        if info[new_r][new_c] > 0 and visited[new_r][new_c] == 0:
                            visited[new_r][new_c] = 1
                            start.append([new_r, new_c])
    if count == 0:
        print(0)
        break
    
    elif count >= 2:
        print(result)
        break
             
    result += 1
