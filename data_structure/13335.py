# 13335
import sys
from collections import deque
m = sys.stdin.readline

t, l, w = map(int, m().split())
t_info = deque(map(int, m().split()))

time = 0
bridge = deque([0]) * l
while True:
    w += bridge.popleft()
    if t_info and w >= t_info[0]:
        t = t_info.popleft()
        bridge.append(t)
        w -= t
        
    else:
        bridge.append(0)
    
    time += 1
    if max(bridge) == 0:
        break
print(time)
