# 11052
import sys
m = sys.stdin.readline

card = int(m())
info = [0] + list(map(int, m().split()))
answer = [0] * (card+1)

for i in range(1, card+1):
    for j in range(i, card+1):
        if i == j:
            answer[j] = max(info[i], answer[j])
        
        else:
            answer[j] = max(answer[j], answer[j-i] + info[i])

print(answer[-1])
