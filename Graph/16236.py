# 아기상어

import sys
import time
from collections import deque
m = sys.stdin.readline

size = int(m())

water, start = [], deque([])
weight = 2
for _ in range(size):
    water.append(list(map(int, m().split(' '))))

for i in range(size):
    for j in range(size):
        # 아기 상어 위치 저장
        if water[i][j] == 9:
            water[i][j] = 0
            start.append([i, j])

move_y, move_x = [-1, 0, 1, 0], [0, -1, 0, 1]

answer, feed = 0, 0
visited = []
status = False
t = 0
while start:
    start = deque(sorted(start, key=lambda x: (x[0], x[1])))
    for _ in range(len(start)):
        s = start.popleft()
        row, col = s[0], s[1]
        visited.append([row, col])

        # 이동한 곳에 고기가 있고, 더 작다면 - 데이터 삭제 + 시간 갱신 + 위치정보 변경
        if 0 < water[row][col] < weight:
            water[row][col] = 0
            start = deque()
            feed += 1
            visited = [[row, col]]
            status = True
            answer = t
            # 몸집이 커지는 조건
            if feed == weight:
                weight += 1
                feed = 0
        
        for k in range(4):
            new_row, new_col = row + move_y[k], col + move_x[k]
            if 0 <= new_row < size and 0 <= new_col < size and water[new_row][new_col] <= weight:
                if [new_row, new_col] not in visited:
                    start.append([new_row, new_col])
                    visited.append([new_row, new_col])
        if status:
            status = False
            break
    t += 1
print(answer)
