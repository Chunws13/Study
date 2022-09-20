import sys
from collections import deque
m = sys.stdin.readline

size = int(m())
info = [[0] * size for _ in range(size)]
apple = int(m())

# 사과 정보 기록
for _ in range(apple):
    r, c = map(int, m().split())
    info[r-1][c-1] = 2

# 뱀 움직임 정보 기록
info_2 = int(m())
move_info = deque([list(m().split()) for _ in range(info_2)])

# 움직이는 순서
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
idx = 0

snake = deque([[0, 0]])
time_ = 0
while True:
    time_ += 1
    next_r, next_c = snake[0][0] + move[idx][0], snake[0][1] + move[idx][1]
    
    # 벽을 넘어가는 경우
    if next_r < 0 or next_r >= size or next_c < 0 or next_c >= size or info[next_r][next_c] == 1:
        break
    
    snake.appendleft([next_r, next_c])
    if info[next_r][next_c] != 2:
        r, c = snake.pop()
        info[r][c] = 0
    
    info[next_r][next_c] = 1
    
    while move_info and time_ == int(move_info[0][0]):
        m = move_info.popleft()
        # 인덱스 넘어가기 방지
        if m[1] == 'D':
            idx += 1
            if idx == 4:
                idx = 0
        
        else:
            idx -= 1
            if idx == -1:
                idx = 3
        
print(time_)
