# 14891
import sys
from collections import deque
input = sys.stdin.readline

info = []
for _ in range(4):
    info.append(deque(map(int, input().strip())))

num = int(input())
orders = [list(map(int, input().split())) for _ in range(num)]

def cycle_logic(point, direction):
    if direction == 1:
        info[point].appendleft(info[point].pop())
    
    elif direction == -1:
        info[point].append(info[point].popleft())

def status_set(point, direction, pre):
    if pre == point: # 시작점
        status[point] = direction
        
        status_set(point - 1, direction, point)
        status_set(point + 1, direction, point)
    
    if 0 <= point <= 3 and 0 <= pre <= 3 and status[point] == 0:
        max_point, min_point = max(point, pre), min(point, pre)
        if info[min_point][2] == info[max_point][6]:
            status[point] = 0
        
        else:
            status[point] = -direction
            status_set(point - 1, -direction, point)
            status_set(point + 1, -direction, point)
            
        
status = [0, 0, 0, 0]
for target, order in orders:
    status_set(target-1, order, target-1)
    for k in range(4):
        cycle_logic(k, status[k])
    status = [0, 0, 0, 0]
    
answer = 0
for i in range(4):
    if info[i][0] == 1:
        answer += 2 ** i

print(answer)
