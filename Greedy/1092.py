from collections import deque
import sys
m = sys.stdin.readline

crane_num = int(m())
crane = list(map(int, m().split()))

box_num = int(m())
box = deque(sorted(list(map(int, m().split())), reverse=True))

crane.sort(reverse = True)

time, index = 1, 0

if box[0] > crane[0]:
    print(-1)
    sys.exit()

tmp = deque()

while box or tmp:
    if len(box) == 0:
        box, tmp = tmp, deque()
        index = 0
        time += 1
        
    b = box.popleft()
    
    if b > crane[index]:
        tmp.append(b)
    
    else:
        index += 1
        
    if index == crane_num:
        index = 0
        time += 1
        box, tmp = tmp + box, deque()
    
if index == 0:
    time -= 1

print(time)
