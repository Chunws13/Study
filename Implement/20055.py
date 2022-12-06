# 20055
import sys
input = sys.stdin.readline

size, limit = map(int, input().split())
info = list(map(int, input().split()))
belt = [0] * (size * 2)

def rotate():
    origin = belt[:]
    origin_info = info[:]
        
    for i in range(size * 2):
        next = (i + 1) % (size * 2)
        belt[next] = origin[i]
        info[next] = origin_info[i]
    
    if belt[size-1]:
        belt[size-1] = 0
    
def move():
    for i in range(size*2 -1, -1, -1):
        next = (i + 1) % (size * 2)
        if belt[i] == 0:
            continue
        
        if belt[next] or info[next] == 0:
            continue
        
        belt[i], belt[next] = 0, 1
        info[next] -= 1
        
        if belt[size-1]:
           belt[size-1] = 0
    
def add_robot():
    if info[0] > 0 and belt[0] == 0:
        belt[0] = 1
        info[0] -= 1
        
def check():
    if info.count(0) >= limit:
        return True
    return False

cycle = 1
while True:
    rotate()
    move()
    add_robot()
    status = check()
    
    if status:
        break
    cycle += 1

print(cycle)
