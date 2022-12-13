# 21610
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(m)]

ad_r, ad_c = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
side_r, side_c = [-1, -1, 1, 1], [-1, 1, -1, 1]

def move(c, d, move):
    new_poistion = []
    for row, col in c:
        new_row, new_col = (row + (ad_r[d]) * move) % n, (col + (ad_c[d] * move)) % n
        new_poistion.append([new_row, new_col])
    return new_poistion
    
def copy_bug(c):
    for row, col in c:
        count = 0
        for i in range(4):
            new_r, new_c = row + side_r[i], col + side_c[i]
            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
                continue
            if info[new_r][new_c] == 0:
                continue
            
            count += 1
        info[row][col] += count
            
def make_cloud(c):
    new_cloud = []
    visited = [[0] * n for _ in range(n)]
    for row, col in c:
        visited[row][col] = 1
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                continue
            
            if info[i][j] >= 2:
                info[i][j] -= 2
                new_cloud.append([i, j])
    
    return new_cloud

cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
for direction, moving in orders:
    new_position = move(cloud, direction-1, moving)
    
    for r, c in new_position:
        info[r][c] += 1
    
    copy_bug(new_position)
    cloud = make_cloud(new_position)

print(sum(map(sum, info)))
    
