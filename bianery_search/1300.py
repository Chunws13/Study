import sys
input = sys.stdin.readline

n, k = int(input()), int(input())

left, right = 0, n ** 2
result = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, n +1): # 2차원 배열을 가정하고, K 이하 수 
        cnt += min(mid // i, n)
    
    if cnt >= k:
        result = mid
        right = mid - 1

    else:
        left = mid + 1

print(result)
