import sys
input = sys.stdin.readline

n, c = map(int, input().split())
info = sorted([int(input()) for _ in range(n)])

left, right = min(info[-1] - info[-2], info[1] - info[0]), info[-1] - info[0]
result = 0

while left <= right:
    mid = (left + right) // 2
    value = info[0]
    count = 1
    for i in range(1, n):
        if info[i] >= value + mid:
            value = info[i]
            count += 1
    
    if count >= c:
        left = mid + 1
        result = mid
    
    else:
        right = mid - 1
        
print(result)
