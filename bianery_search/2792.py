import sys
input = sys.stdin.readline

n, m = map(int, input().split())
total = [int(input()) for _ in range(m)]

result = 0
left, right = 1, max(total)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    if mid == 0:
        break

    for t in total:
        cnt += (t // mid)
        cnt += min(t % mid, 1)
    
    if cnt > n:
        left = mid + 1
    
    else:
        result = mid
        right = mid - 1

print(result)
