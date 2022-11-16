# 17406
from itertools import permutations
import sys, copy
m = sys.stdin.readline

r, c, s = map(int, m().split())
info = [[0] * (c+1)] + [[0] + list(map(int, m().split())) for _ in range(r)]
order_list = [list(map(int, m().split())) for _ in range(s)]

def rotate(r, c, s, origin):
    info = copy.deepcopy(origin)
    while s:
        row, col, cnt = r-s, c-s, 0
        origin_list, change_value = [[row, col]], [info[row+1][col]]
        
        while cnt // (s*2) < 4:
            change_value.append(info[row][col])
            
            if cnt // (s*2) < 1: 
                col += 1
                
            elif cnt // (s*2) < 2: 
                row += 1
            
            elif cnt // (s*2) < 3: 
                col -= 1
            
            else: 
                row -= 1
                
            origin_list.append([row, col])
            cnt += 1

        for i, j in zip(origin_list[:-1], change_value[:-1]):
            info[i[0]][i[1]] = j
        
        s -=1
        
    return info
all_order_list = list(permutations(order_list, len(order_list)))
answer = 10 ** 6
for order in all_order_list:
    tmp = copy.deepcopy(info)
    for r, c, s in order:
        tmp = rotate(r, c, s, tmp)
        
    answer = min(answer, min(map(sum, tmp[1:])))

print(answer)
