# 11501
import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    num = int(input())
    cost = list(map(int, input().split()))
    
    empty_answer = [0] * num
    max_value, answer = 0, 0
    for c in range(num-1, -1, -1):
        max_value = max(max_value, cost[c])
        empty_answer[c] = max_value
    
    for i in range(num):
        answer += empty_answer[i] - cost[i]

    print(answer)
