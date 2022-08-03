# 강의실 2
import sys
import heapq

m = sys.stdin.readline

class_num = int(m())
info = [list(map(int, m().split())) for _ in range(class_num)]

start, end = [], []

for i in info:
    n, s, e = map(int, i)
    heapq.heappush(start, [s, e, n])

c_info = [0] * class_num
room = 1
while start:
    s, e, n = heapq.heappop(start)
    if len(end) == 0:
        heapq.heappush(end, [e, s, n, room])
        room += 1
        
    elif s >= end[0][0]:
        f = heapq.heappop(end)
        c_info[f[2]-1] = f[-1]
        heapq.heappush(end, [e, s, n, f[-1]])
    
    else:
        heapq.heappush(end, [e, s, n, room])
        room += 1
print(len(end))
while end:
    f = heapq.heappop(end)
    c_info[f[2]-1] = f[-1]
    
for c in c_info:
    print(c)
