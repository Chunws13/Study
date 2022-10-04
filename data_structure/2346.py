import sys
from collections import deque
m = sys.stdin.readline

b = int(m())
next_pop = deque(map(int, m().split()))
info = deque([i+1 for i in range(b)])

answer = []
while info:
    k = next_pop.popleft()
    answer.append(info.popleft())
    
    if k < 0:
        while info and abs(k) != 0:
            i = info.pop()
            info.appendleft(i)
            
            n = next_pop.pop()
            next_pop.appendleft(n)
            k += 1
        
    else:
        while info and abs(k)-1 != 0:
            i = info.popleft()
            info.append(i)
            
            n = next_pop.popleft()
            next_pop.append(n)
            k -= 1
    
print(" ".join(map(str, answer)))
