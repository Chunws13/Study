#10942
import sys
m = sys.stdin.readline
num = int(m())

info = [0] + list(map(int, m().split()))
problem = int(m())

# 배열 초기화
answer = [[0] * (num+1) for _ in range(num+1)]
for i in range(1, num+1):
    answer[i][i] = 1

for i in range(1, num):
    if info[i] == info[i+1]:
        answer[i][i+1] = 1

for i in range(num, 0, -1):
    for j in range(num, i, -1):
        if info[i] != info[j]:
            answer[i][j] = 0
        
        elif answer[i+1][j-1] == 1:
            answer[i][j] = 1
            
    
# 입력 받기
results = []
for i in range(problem):
    a, b = map(int, m().split())
    results.append(answer[a][b])

for result in results:
    print(result)
