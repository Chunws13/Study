# 2169
import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, m):
    info[0][i] += info[0][i-1]
    

for i in range(1, n):
    left_move, right_move = copy.deepcopy(info[i][:]), copy.deepcopy(info[i][:])
    
    for j in range(m): # 좌 > 우
        if j == 0:
            left_move[j] += info[i-1][j]
        
        else:
            left_move[j] += max(info[i-1][j], left_move[j-1])
    
    for j in range(m-1, -1, -1): # 우 > 좌
        if j == m-1:
            right_move[j] += info[i-1][j]
            
        else:
            right_move[j] += max(info[i-1][j], right_move[j+1])
    
    for j in range(m):
        info[i][j] = max(left_move[j], right_move[j])

print(info[-1][-1])
