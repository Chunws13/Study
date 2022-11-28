# 2638
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(row)]

# 1. 치즈 외부 공간 우선 계산 > -1 처리
# 2. -1 면적 2 이상 표기 > 삭제
# 3. 1 ~ 2 과정 반복
ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]


def outer_find():
    global cheese
    start = [[0, 0]]
    visited = [[0] * col for _ in range(row)]
    cheese[0][0] = -1
    outer = []
    while start:
        r, c = start.pop()
        for l in range(4):
            new_r, new_c = ad_r[l] + r,  ad_c[l] + c
            if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:
                continue    
            
            if visited[new_r][new_c]:
                continue
            
            if cheese[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                start.append([new_r, new_c])
                outer.append([new_r, new_c])

    for o_r, o_c in outer:
        cheese[o_r][o_c] = -1
    
def melt():
    global cheese
    melt_point = []
    for i in range(row):
        for j in range(col):
            if cheese[i][j] != 1:
                continue
            point = 0
            for k in range(4):
                new_r, new_c = ad_r[k] + i,  ad_c[k] + j
                if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:
                    continue
                
                if cheese[new_r][new_c] == -1:
                    point += 1
            
            if point >= 2:
                melt_point.append([i, j])
            
    for m_r, m_c in melt_point:
        cheese[m_r][m_c] = 0
    
    if melt_point:
        return False
    
    else:
        return True
    
def set_origin():
    global cheese
    for i in range(row):
        for j in range(col):
            if cheese[i][j] == -1:
                cheese[i][j] = 0
             
answer = 1
while True:
    outer_find()
    status = melt()
    if status:
        answer -= 1
        break
    
    else:
        answer += 1
        set_origin()

print(answer)
