# 2156
import sys
m = sys.stdin.readline

wine = int(m())
info = [int(m()) for _ in range(wine)]
answer = [0] * wine

for i in range(wine):
    if i == 0:
        answer[i] = info[i]
    
    elif i == 1:
        answer[i] = info[i] + info[i-1]

    elif i == 2:
        answer[i] = max(info[i-1]+info[i], info[i-2]+info[i], answer[i-1])
    
    else:
        answer[i] = max(info[i] + info[i-1] + answer[i-3], answer[i-2] + info[i], answer[i-1])

print(max(answer))
