# 2696
import sys
import heapq

m = sys.stdin.readline

case = int(m())
answer = []
for _ in range(case):
    list_len = int(m())
    info = list(map(int, m().split()))
    while list_len > 10:
        info += list(map(int, m().split()))
        list_len -= 10
    
    left, right, tmp = [], [], []
    for i in range(len(info)):
        if len(left) == len(right):
            heapq.heappush(left, -info[i])
        
        else:
            heapq.heappush(right, info[i])
    
        if left and right and -left[0] > right[0]:
            l = heapq.heappop(left)
            r = heapq.heappop(right)
            heapq.heappush(right, -l)
            heapq.heappush(left, -r)
        
        if i%2 == 0:
            tmp.append(-left[0])
    print(len(tmp))
    for a in range(0, len(tmp), 10):
        print(" ".join(map(str, tmp[a:a+10])))
