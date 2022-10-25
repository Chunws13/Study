# 10844
import sys
m = sys.stdin.readline

info = int(m())
answer = [[0] + [1] * 9]
for i in range(1, info):
    answer.append([0] * 10)

for i in range(1, info):
    for j in range(10):
        for k in [1, -1]:
            if j + k < 0 or j + k > 9:
                continue
            
            answer[i][j] = (answer[i][j] + answer[i-1][j+k])%1000000000

print(sum(answer[-1])%1000000000)
