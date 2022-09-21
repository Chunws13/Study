import sys
import heapq
m = sys.stdin.readline

num = int(m())
left, right = [], []
answer = []

for _ in range(num):
    number = int(m())
    if len(left) == len(right):
        heapq.heappush(right, -number)
    
    else:
        heapq.heappush(left, number)
    
    while left and left[0] < -right[0]:
        r_to_l = heapq.heappop(right)
        l_to_r = heapq.heappop(left)
        
        heapq.heappush(left, -r_to_l)
        heapq.heappush(right, -l_to_r)
        
    answer.append(-right[0])

for i in answer:
    print(i)
