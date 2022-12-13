# 20056
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(m)]

ad_r, ad_c = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def move(r, c, mas, sp, dir):
    new_r, new_c = (r + ad_r[dir] * sp) % n, (c + ad_c[dir] * sp) % n
    board[new_r][new_c][0] += mas
    board[new_r][new_c][1] += sp
    board[new_r][new_c][2] += [dir]
    return [new_r, new_c]

def despense():
    d_point = []
    for r in range(n):
        for c in range(n):
            mas, sp, dir = board[r][c]
            
            if len(board[r][c][2]) == 1:
                d_point.append([r, c, mas, sp, dir[0]])
                continue
            
            if len(board[r][c][2]) >= 2:
                if board[r][c][0] < 5:
                    continue
            
                dire = 0 if check(board[r][c][2]) else 1
                    
                mas, sp = mas // 5, sp // len(board[r][c][2])
                
                for i in range(dire, 8, 2):
                    d_point.append([r, c, mas, sp, i])
        
    return d_point

def check(check_list):
    for c in range(len(check_list)-1):
        if check_list[c] % 2 != check_list[c+1] % 2:
            return False
    
    return True
        

for f in range(len(fireball)):
    fireball[f][0] -= 1
    fireball[f][1] -= 1

for _ in range(k):
    board = [[[0, 0, []] for _ in range(n)] for _ in range(n)] # mass, direction, speed
    
    for row, col, mass, speed, direction in fireball:
        move(row, col, mass, speed, direction)

    fireball = despense()
    
answer = 0        
for f in fireball:
    answer += f[2]
print(answer)
