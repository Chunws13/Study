# 1103
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
table = [[0] * c for _ in range(r)]

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

status = False
def find_logic(row, col, result):
    global status
    move = int(board[row][col])
    
    for i in range(4):
        new_r, new_c = row + ad_r[i] * move, col + ad_c[i] * move
        if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c or board[new_r][new_c] == 'H':
            continue
        
        if result + 1 > table[new_r][new_c]:
            if visited[new_r][new_c]:
                status = True
                return
            
            visited[new_r][new_c] = 1
            table[new_r][new_c] = result + 1
            find_logic(new_r, new_c, result + 1)
            visited[new_r][new_c] = 0

table[0][0] = 1
find_logic(0, 0, 1)
if status:
    print(-1)
else:
    print(max(map(max, table)))
