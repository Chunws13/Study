#2096
import sys
import math
from collections import deque
m = sys.stdin.readline

size = int(m())
inf = math.inf
answer = deque([[[inf,0], [inf,0], [inf,0]]])

for i in range(size):
    info = list(map(int, m().split()))
    if i == 0:
        for j in range(3):
            answer[i][j][0], answer[i][j][1] = info[j], info[j]
            continue
    
    else:
        answer.append([[inf,0], [inf,0], [inf,0]])
        for j in range(3):
            for k in range(j-1, j+2):
                if k < 0 or k > 2:
                    continue

                answer[1][j][0] = min(answer[0][k][0] + info[j], answer[1][j][0])
                answer[1][j][1] = max(answer[0][k][1] + info[j], answer[1][j][1])

        answer.popleft()

print(max(map(max, answer[-1])), min(map(min, answer[-1])), sep = ' ')
