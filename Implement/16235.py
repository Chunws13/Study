# 16235
# list + deque 로 풀었으나
# list + dic 구조가 더 빠른 것으로 보임 (정답 리스트 참고, 한 칸 당 데이터 길이가 줄어서..?)
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

ground = [[5] * n for _ in range(n)]
seed = [list(map(int, input().split())) for _ in range(n)]
trees = [[deque([]) for _ in range(n)]  for _ in range(n)]
for _ in range(m):
    row, col, year = map(int, input().split())
    trees[row-1][col-1].append(year)

adr, adc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]


y = 0
while y < k:
    new_trees = deque([])
    
    for i in range(n):
        for j in range(n):
            
            d_trees = deque([])
            
            for _ in range(len(trees[i][j])):
                year = trees[i][j].popleft()
                
                if ground[i][j] < year:
                    d_trees.append(year // 2)
                    continue
                
                ground[i][j] -= year
                trees[i][j].append(year + 1)
                
                if (year + 1) % 5 == 0:
                    new_trees.append([i, j])
            
            for d in d_trees:
                ground[i][j] += d
                
    for row , col in new_trees:
        for ki in range(8):
            new_r, new_c = row + adr[ki], col + adc[ki]
            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
                continue
            
            trees[new_r][new_c].appendleft(1)
    
    for row in range(n):
        for col in range(n):
            ground[row][col] += seed[row][col] 
    
    y += 1
    
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)
