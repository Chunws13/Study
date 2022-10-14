#11054
import sys
m = sys.stdin.readline

num = int(m())
info = list(map(int, m().split()))
answer = [0] * num

for i in range(num):
    for j in range(i):
        if info[i] > info[j]:
            answer[i] = max(answer[j], answer[i])
        
    answer[i] += 1
    
for i in range(num):
    for j in range(i):
        if info[i] < info[j]:
            answer[i] = max(answer[j]+1, answer[i])
    

print(max(answer))
