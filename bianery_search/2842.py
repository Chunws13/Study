# 2842
import sys, math, copy
from collections import deque
input = sys.stdin.readline

n = int(input())

point = [list(map(str, input().strip())) for _ in range(n)]
height = [list(map(int, input().split())) for _ in range(n)]

start, target = deque([]), 0
tmp_list = set() # 고도 최대 1,000,000으로 높이 정보를 담은 set 생성 > 탐색 시간 

for i in range(n):
    for j in range(n):
        tmp_list.add(height[i][j])
        if point[i][j] == 'P':
            start.append([i, j])
        
        if point[i][j] == 'K':
            target += 1

adr, adc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

def finder(start, left, right, target):
    t = 0
    visited = [[0] * n for _ in range(n)]
    s = copy.deepcopy(start)
        
    while s:
        r, c = s.popleft()
        
        if height[r][c] > right or height[r][c] < left:
            return False

        for k in range(8):
            new_r, new_c = r + adr[k], c + adc[k]
            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n or visited[new_r][new_c]:
                continue

            if left <= height[new_r][new_c] <= right:
                visited[new_r][new_c] = 1
                if point[new_r][new_c] == 'K':
                    t += 1
                
                if t == target:
                    return True

                s.append([new_r, new_c])
    
    return False

h_list = sorted(tmp_list)
result = math.inf

left, right = 0, 0
while right < len(h_list) and left < len(h_list):
    if finder(start, h_list[left], h_list[right], target):
        result = min(result, h_list[right] - h_list[left])
        left += 1
    
    else:
        right += 1

print(result)
