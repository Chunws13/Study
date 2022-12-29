# 13460
import sys, math
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]

red, blue, goal = 0, 0, 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'R':
            red = [i, j]
        
        if board[i][j] == 'B':
            blue = [i, j]
        
        if board[i][j] == 'O':
            goal = [i, j]
            
ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

def move2(marble, d):
    m_count = 1
    row, col = marble[0], marble[1]
    while True:
        row, col = row + ad_r[d] , col + ad_c[d]
        # print(row, col)
        if board[row][col] == 'O':
            break
        
        if board[row][col] == '#':
            row, col = row - ad_r[d], col - ad_c[d]
            break
        
        m_count += 1
        
    return row, col, m_count
    
def move(red, blue, d): # 동시에 움직임
    r_row, r_col, r_m = move2(red, d)
    b_row, b_col, b_m = move2(blue, d)
    
    if [r_row, r_col] == goal or [b_row, b_col] == goal:
        return [r_row, r_col], [b_row, b_col]
        
    if [r_row, r_col] == [b_row, b_col]:
        if r_m > b_m:
            r_row, r_col = r_row - ad_r[d], r_col - ad_c[d]
        
        else:
            b_row, b_col = b_row - ad_r[d], b_col - ad_c[d]
            
    return [r_row, r_col], [b_row, b_col]

answer = math.inf
def solve(red, blue, chance):
    global answer
    if chance > 10:
        return 
    
    for i in range(4):
        new_red, new_blue = move(red, blue, i)
        if new_blue == goal:
            continue
        
        if new_red == goal:
            answer = min(answer, chance)
            continue
        
        solve(new_red, new_blue, chance + 1)
solve(red, blue, 1)

if answer == math.inf:
    print(-1)
    
else:
    print(answer)
