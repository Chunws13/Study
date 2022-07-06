# Triange.py 와 동일한 문제

import sys
m = sys.stdin.readline

size = int(m())
triangle = [list(map(int, m().split(' '))) for _ in range(size)]
answer = [[0] * i for i in range(1, size+1)]

for j in range(len(triangle)):
    for k in range(len(triangle[j])):

        if j == 0:
            answer[j][0] = triangle[j][0]
        
        else:
            if k == 0:
                answer[j][k] = answer[j-1][0] + triangle[j][k]
            
            elif k == len(triangle[j])-1:
                answer[j][k] = answer[j-1][-1] + triangle[j][k]
                
            else:
                answer[j][k] = max(answer[j-1][k-1] + triangle[j][k], answer[j-1][k] + triangle[j][k])
                
print(max(answer[-1]))
