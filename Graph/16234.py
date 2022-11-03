# 16234
import sys
m = sys.stdin.readline

n, l, r = map(int, m().split())
nation = []
for _ in range(n):
    nation.append(list(map(int, m().split())))

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

status = True
result = 0
while status:
    visit = [[0] * (n) for _ in range(n)]
    move = []
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 1:
                continue
            
            visit[i][j] = 1
            start, tmp_list = [[i, j]], [[i, j]]
            
            while start:
                row, col = start.pop()
                for k in range(4):
                    new_r, new_c = row + ad_r[k], col + ad_c[k]
                    if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
                        continue
                    
                    if visit[new_r][new_c] == 1:
                        continue
                    
                    if l <= abs(nation[row][col] - nation[new_r][new_c]) <= r:
                        visit[new_r][new_c] = 1
                        start.append([new_r, new_c])
                        tmp_list.append([new_r, new_c])
                        
            if len(tmp_list) > 1:
                move.append(tmp_list)
    
    if len(move):
        result += 1
        for i in move:
            people = 0
            for row, col in i:
                people += nation[row][col]
            
            people = int(people/len(i))
            
            for row, col in i:
                nation[row][col] = people
        
    else:
        status = False
print(result)
