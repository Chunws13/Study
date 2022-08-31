import sys
from collections import deque
m = sys.stdin.readline

member = int(m())
a_team = deque(sorted(list(map(int, m().split()))))
b_team = sorted(list(map(int, m().split())))

for_draw = deque([])
answer = 0

while a_team:
    a = a_team.popleft()
    pop_index = -1
    for b in range(len(b_team)):
        if b_team[b] < a:
            pop_index = b
        
    if pop_index != -1:
        b_team.pop(pop_index)
        answer += 2
    
    else:
        for_draw.append(a)
            
while for_draw:
    f = for_draw.popleft()
    for b in range(len(b_team)):
        if b_team[b] == f:
            b_team.pop(b)
            answer += 1
            break

print(answer)
