import sys, math
input = sys.stdin.readline

size, limit = map(int,input().split())
info = list(map(int, input().split()))

left, right = 0, sum(info)
max_value = max(info)
answer = math.inf

while left <= right:
    mid = (left + right) // 2
    
    if mid < max_value: # 중간 조건이 강의 하나보다 작은 경우
        left = mid + 1
        continue

    ray, tmp = 1, 0

    
    for i in info:
        if tmp + i <= mid:
            tmp += i

        else:
            tmp = i
            ray += 1

    if ray > limit: # 블루레이 개수가 많음
        left = mid + 1
    
    else: # 블루레이 개수가 같거나 적음
        right = mid - 1
        answer = min(answer, mid)

print(answer) 
