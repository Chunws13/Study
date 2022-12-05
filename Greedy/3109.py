# 3109
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
info = [list(map(str, input().strip())) for _ in range(row)]

ad_r, ad_c = [1, 0, -1], [1, 1, 1]
answer = 0

for i in range(row):
    start = [[i, 0]]
    while start:
        r, c = start.pop()
        info[r][c] = 'x'
        
        if c == col-1:
            answer += 1
            break
        
        for j in range(3):
            new_r, new_c = ad_r[j] + r, ad_c[j] + c
            if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:
                continue
            
            if info[new_r][new_c] == 'x':
                continue
            
            start.append([new_r, new_c])
    
print(answer)
