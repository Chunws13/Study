# 17144
import sys, copy
input = sys.stdin.readline

r, c, t = map(int, input().split())

condition = [list(map(int, input().split())) for _ in range(r)]

air_cleaner = []
ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if condition[i][j] == -1:
            air_cleaner.append([i, j])

def deffusion(dirty):
    diffues_volum = [[0] * c for _ in range(r)] # 동시 확산을 위해 임시 
    for row, col in dirty:
        origin_volum = condition[row][col]
        tmp = 0
        
        for k in range(4):
            new_r, new_c = row + ad_r[k], col + ad_c[k]
            if new_r < 0 or new_r >=r or new_c < 0 or new_c >= c:
                continue
            
            if condition[new_r][new_c] == -1:
                continue
            
            diffues_volum[new_r][new_c] += origin_volum//5
            tmp += origin_volum//5
        
        condition[row][col] -= tmp
    for row in range(r):
        for col in range(c):
            condition[row][col] += diffues_volum[row][col]
            
def flow(air_cleaner):
    for i in range(2):
        sr, sc = air_cleaner[i]
        if i == 0:
            if sc == 0:
                sr, sc, idx = sr - 1, sc, 0

            else:
                sr, sc, idx = sr, sc - 1, 3
            
            mr, mc = [-1, 0, 1, 0], [0, 1, 0, -1]
        
            while [sr, sc] != air_cleaner[i]:
                if sr + mr[idx] == air_cleaner[i][0] and sc + mc[idx] == air_cleaner[i][1]:
                    break
                    
                elif 0 <= sr + mr[idx] <= air_cleaner[i][0] and 0 <= sc + mc[idx] < c:
                    condition[sr][sc] = condition[sr + mr[idx]][sc + mc[idx]]
                    condition[sr + mr[idx]][sc + mc[idx]] = 0
                    sr, sc = sr + mr[idx], sc + mc[idx]

                else:
                    idx = (idx + 1) % 4
        else:
            if sc == 0:
                sr, sc, idx = sr + 1, sc, 0

            else:
                sr, sc, idx = sr, sc - 1, 3

            mr, mc = [1, 0, -1, 0], [0, 1, 0, -1]

            while [sr, sc] != air_cleaner[i]:
                if sr + mr[idx] == air_cleaner[i][0] and sc + mc[idx] == air_cleaner[i][1]:
                    break
                
                elif air_cleaner[i][0] <= sr + mr[idx] < r and 0 <= sc + mc[idx] < c:
                    condition[sr][sc] = condition[sr + mr[idx]][sc + mc[idx]]
                    condition[sr + mr[idx]][sc + mc[idx]] = 0
                    sr, sc = sr + mr[idx], sc + mc[idx]

                else:
                    idx = (idx + 1) % 4

def check():
    dirty = []
    for i in range(r):
        for j in range(c):
            if condition[i][j] >= 5:
                dirty.append([i, j])

    return dirty

for _ in range(t):
    d_list = check()
    deffusion(d_list)
    flow(air_cleaner)
    
answer = 0
for i in range(r):
    for j in range(c):
        if condition[i][j] > 0:
            answer += condition[i][j]

print(answer)
