# 1309 동물원

import sys

m = sys.stdin.readline
size = int(m())

answer = [[0,0]]

for a in range(size):
    # 없음, 좌, 우 
    if a == 0:
        answer.append([1,2])
    
    else:
        c = sum(answer[a]) %9901
        d = (answer[a][0] * 2 + answer[a][1]) %9901
        answer.append([c, d])

print(sum(answer[size])%9901)
