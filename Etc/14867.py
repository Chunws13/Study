import sys
from collections import deque
input = sys.stdin.readline

a, b, target_a, target_b = map(int, input().split())

# x 채우기 / x 버리기 / x > y 이동
start = deque([[0, 0, 0]])

answer = []
visited = set()
visited.add((0, 0))

while start:
    tried, now_a, now_b = start.popleft()
    
    if now_a == target_a and now_b == target_b:
        answer.append(tried)
        break

    for i in range(6):
        if i == 0:
            if (a, now_b) not in visited:
                visited.add((a, now_b))
                start.append([tried + 1, a, now_b])
        
        elif i == 1:
            if (now_a, b) not in visited:
                visited.add((now_a, b))
                start.append([tried + 1, now_a, b])
        
        elif i == 2: # empty
            if (0, now_b) not in visited:
                visited.add((0, now_b))
                start.append([tried + 1, 0, now_b])
        
        elif i == 3: 
            if (now_a, 0) not in visited:
                visited.add((now_a, 0))
                start.append([tried + 1, now_a, 0])
        
        elif i == 4: # a -> b
            now_a, now_b = max(0, now_a + now_b - b), min(now_a + now_b, b)
            if (now_a, now_b) not in visited:
                visited.add((now_a, now_b))
                start.append([tried + 1, now_a, now_b])
        else:
            now_a, now_b = min(now_a + now_b , a), max(0, now_a + now_b - a)
            if (now_a, now_b) not in visited:
                visited.add((now_a, now_b))
                start.append([tried + 1, now_a, now_b])
    
if answer:
    answer.sort()
    print(answer[0])

else:
    print(-1)
