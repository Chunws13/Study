import sys
from collections import deque
m = sys.stdin.readline

size = int(m())
num_list = deque(map(int, m().split()))

k = 0
answer, stack = [0] * size, []
while num_list:
    n = num_list.popleft()
    
    stack.append([k, n])
    k += 1
    
    while stack and num_list and stack[-1][-1] < num_list[0]:
        s = stack.pop()
        answer[s[0]] = num_list[0]
        
while stack:
    s = stack.pop()
    answer[s[0]] = -1
    
print(" ".join(map(str, answer)))
