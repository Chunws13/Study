import sys, heapq
from collections import deque
input = sys.stdin.readline

start, end = map(int, input().split())

if start == end:
    print(0)
    sys.exit()
    
new_start = deque([['', start]])
visited = set()
visited.add(start)

cal = ['*', '+', '-', '/']
answer = -1
new_answer = []

while new_start:
    times, now = new_start.popleft()
    if now == end:
        new_answer.append(times)
    
    elif now > 10 ** 9:
        continue
        
    for i in range(4):
        if cal[i] == '+':
            num = now + now
            if num not in visited:
                visited.add(num)
                new_start.append([times + cal[i], num])
                # heapq.heappush(new_start, [times + cal[i], num])
        
        elif cal[i] == '-':
            num = 0
            if num not in visited:
                visited.add(num)
                new_start.append([times + cal[i], num])
                # heapq.heappush(new_start, [times + cal[i], num])
        
        elif cal[i] == '*':
            num = now ** 2
            if num not in visited:
                visited.add(num)
                new_start.append([times + cal[i], num])
                # heapq.heappush(new_start, [times + cal[i], num])
        
        else:
            if now == 0:
                continue
            
            num = 1
            if num not in visited:
                visited.add(num)
                new_start.append([times + cal[i], num])
                # heapq.heappush(new_start, [times + cal[i], num])

if new_answer:
    new_answer.sort()
    print(new_answer[0])

else:
    print(answer)
