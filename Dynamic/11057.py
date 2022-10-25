# 11057
import sys
m = sys.stdin.readline

info = int(m())
answer = [1] * 10

for i in range(1, info):
    for j in range(1, 10):
        answer[j] += answer[j-1]
        
print(sum(answer)%10007)
