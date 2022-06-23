# 1520 내리막길

import sys
sys.setrecursionlimit(10**8)
m = sys.stdin.readline

row, col = map(int, m().split(' '))

map_info = []
answer = []
for r in range(row):
    map_info.append(list(map(int, m().split(' '))))
    answer.append([-1] * col)

x, y = [1, -1, 0, 0], [0, 0, 1, -1]

def solution(r, c):
    if r == row-1 and c == col-1:
        return 1

    if answer[r][c] == -1:
        answer[r][c] = 0
        for i in range(4):
            ad_x, ad_y = c + x[i], r + y[i]
            
            if 0 <= ad_x < col and 0 <= ad_y < row and map_info[r][c] > map_info[ad_y][ad_x]:
                    answer[r][c] += solution(ad_y, ad_x)
    
    return answer[r][c]

print(solution(0, 0))
