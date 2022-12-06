# 20057
import sys, math
input = sys.stdin.readline

size = int(input())
info = [list(map(int, input().split())) for _ in range(size)]

ad_r, ad_c = [0, 1, 0, -1], [-1, 0, 1, 0]
row, col = size // 2, size // 2

count, idx, limit, l_count = 0, 0, 1, 0
answer = 0

wind = [[0, 0, 0.02, 0 ,0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 0, 0, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0]]

# 배열 회전
def rotate(o_list, index):
    n = len(o_list) # row
    m = len(o_list[0]) # col
    new = [[0] * n for _ in range(m)]
    
    if index == 1:
        for i in range(n):
            for j in range(m):
                new[m-j-1][i] = o_list[i][j]
        return new
        
    elif index == 2:
        for i in range(n):
            for j in range(m):
                new[n-i-1][m-j-1] = o_list[i][j]
        return new
        
        
    elif index == 3:
        for i in range(n):
            for j in range(m):
                new[j][n-i-1] = o_list[i][j]
        return new
    
    else:
        return o_list    


def send(row, col, idx):
    global answer
    new_wind = rotate(wind, idx)
    
    standard, mod = info[row][col], info[row][col]
    
    for i in range(5):
        for j in range(5):
            new_r , new_c = row + i -2, col + j - 2
            sand = math.floor(standard * new_wind[i][j])
            mod -= sand
            if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:
                answer += sand
                continue
            
            info[new_r][new_c] += sand
    
    mod_r, mod_c = row + ad_r[idx], col + ad_c[idx]
    if mod_r < 0 or mod_r >= size or mod_c < 0 or mod_c >= size:
        answer += mod
    
    else:
        info[mod_r][mod_c] += mod
    
    info[row][col] = 0
        
while 0 <= row < size and 0 <= col < size:
    row, col = ad_r[idx] + row, ad_c[idx] + col
    
    send(row, col, idx)
    
    count += 1
    if count == limit:
        count = 0
        l_count += 1
        idx = (idx + 1) % 4
        
        if l_count == 2:
            limit += 1
            l_count = 0

print(answer)
