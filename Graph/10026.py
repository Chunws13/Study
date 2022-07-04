# 색맹 구분 - 함수화해서 간결하게할 

import sys
from collections import deque
m = sys.stdin.readline

size = int(m())
picture, origin_picture = [], []
answer, ab_answer = [], []

for _ in range(size):
    pattern = list(map(str, m().strip()))
    picture.append(pattern)
    origin_picture.append([0] * size)

    answer.append([False] * size)
    ab_answer.append([False] * size)

row, col  = [1, -1, 0, 0], [0, 0, 1, -1]
cnt, ab_cnt = 0, 0
           
for i in range(size):
    for j in range(size):

        if ab_answer[i][j] == False:
            ab_answer[i][j] = True
            ab_cnt += 1

        que = deque([[i, j]])
        while que:
            q = que.popleft()
            r, c = q[0], q[1]

            for k in range(4):
                ad_row, ad_col = r + row[k], c + col[k]
            
                if 0 <= ad_row < size and 0 <= ad_col < size and ab_answer[ad_row][ad_col] == False:
                    if picture[r][c] == picture[ad_row][ad_col]:
                        ab_answer[ad_row][ad_col] = True
                        que.append([ad_row, ad_col])

for i in range(size):
    for j in range(size):
        origin_picture[i][j] = picture[i][j]
        if picture[i][j] != 'B':
            picture[i][j] = 'A'
            for k in range(4):
                ad_row, ad_col = i + row[k], i + col[k]
            
            if 0 <= ad_row < size and 0 <= ad_col < size:
                if picture[ad_row][ad_col] == 'R' or picture[ad_row][ad_col] == 'G':
                    picture[ad_row][ad_col] = 'A'

for i in range(size):
    for j in range(size):
                    
        if answer[i][j] == False:
            answer[i][j] = True
            cnt += 1

        que = deque([[i, j]])
        while que:
            q = que.popleft()
            r, c = q[0], q[1]

            for k in range(4):
                ad_row, ad_col = r + row[k], c + col[k]
                
                if 0 <= ad_row < size and 0 <= ad_col < size and answer[ad_row][ad_col] == False:
                    if picture[r][c] == picture[ad_row][ad_col]:
                        answer[ad_row][ad_col] = True
                        que.append([ad_row, ad_col])

print(ab_cnt, cnt)
