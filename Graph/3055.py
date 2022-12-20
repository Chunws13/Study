# 3055
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]
start, end, water = [], [], []

for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            start.append([i, j])
        
        if board[i][j] == '*':
            water.append([i, j])

def flood(water_point):
    next_point = []
    for row, col in water_point:
        for  i in range(4):
            new_r, new_c = row + ad_r[i], col + ad_c[i]
            if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
                continue
            
            if board[new_r][new_c] == 'X' or board[new_r][new_c] == 'D' or visited[new_r][new_c]:
                continue
                
            board[new_r][new_c] = '*'
            visited[new_r][new_c] = 1
            next_point.append([new_r, new_c])
    
    return next_point

def move(start_point):
    next_point = []
    for row, col in start_point:
        for  i in range(4):
            new_r, new_c = row + ad_r[i], col + ad_c[i]
            if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
                continue
            
            if board[new_r][new_c] == 'X' or board[new_r][new_c] == '*' or visited[new_r][new_c]:
                continue
            
            if board[new_r][new_c] == 'D':
                print(result)
                sys.exit()
                
            visited[new_r][new_c] = 1
            next_point.append([new_r, new_c])
    
    return next_point

visited = [[0] * c for _ in range(r)]
visited[start[0][0]][start[0][1]] = 1

for row, col in water:
    visited[row][col] = 1

result = 1
while start:
    water = flood(water)
    start = move(start)
    result += 1
    
print("KAKTUS")
