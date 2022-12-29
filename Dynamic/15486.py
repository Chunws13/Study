# 15486
import sys
input = sys.stdin.readline

time_limit = int(input())
info = [list(map(int, input().split())) for _ in range(time_limit)]
answer = [0] * (time_limit + 1)

max_value = 0
for i in range(time_limit):
    max_value = max(max_value, answer[i]) # 다음날 전까지 최대 가치
    if info[i][0] + i > time_limit:
        continue
    answer[i + info[i][0]] = max(answer[i + info[i][0]], max_value + info[i][1])
    
print(max(answer))
