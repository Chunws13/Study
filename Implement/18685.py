# 15685
import sys, copy
input = sys.stdin.readline

num = int(input())
info = [list(map(int, input().split())) for _ in range(num)]

ad_r, ad_c = [0, -1, 0, 1], [1, 0, -1, 0]

def gernerate(start, gen, target_gen):
    if gen == target_gen:
        return start
    
    else:
        tmp_list = [start[-1]]
        
        for s in range(len(start)-1, 0, -1):
            row_diff, col_diff = start[s][0] - start[s-1][0], start[s][1] - start[s-1][1]
            tmp_list.append([tmp_list[-1][0] - col_diff, tmp_list[-1][1] + row_diff])
        
        start += tmp_list[1:]
        return gernerate(start, gen+1, target_gen)

board = [[0] * 101 for _ in range(101)]

for col, row, direction, g in info:
    start = [[row, col], [row + ad_r[direction], col + ad_c[direction] ]]
    line = gernerate(start, 0, g)

    for r, c in line:
        board[r][c] = 1

result = 0
check_r, check_c = [0, 0, 1, 1], [0, 1, 0, 1]
for i in range(100):
    for j in range(100):
        answer = 0
        
        for k in range(4):
            new_r, new_c = i + check_r[k], j + check_c[k]
            if new_r < 0 or new_r >= 101 or new_c < 0 or new_c >= 101:
                continue
            
            answer += board[new_r][new_c]
        
        if answer == 4:
            result += 1
        
print(result)
