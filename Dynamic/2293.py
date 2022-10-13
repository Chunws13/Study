#2293
import sys
m = sys.stdin.readline

num, target = map(int, m().split())
coin = [0] + [int(m()) for _ in range(num)]
answer = [0] * (target+1)

for i in range(1, num+1):
    for j in range(1, target+1):
        if j == coin[i]:
            answer[j] += 1
            
        elif j > coin[i]:
            answer[j] = answer[j] + answer[j-coin[i]]
        
print(answer[target])
