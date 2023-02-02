import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
info = list(map(int, input().split()))

left, right = 0, max(info) - min(info)
result = math.inf

while left <= right:
    mid = (left + right) // 2
    cnt, h, l = 1, info[0], info[0]
    for i in info:
        if i > h:
            h = i
        
        if i < l:
            l = i
        
        if h - l > mid:
            cnt += 1
            l, h = i, i
    
    if cnt > m:
        left = mid + 1

    else:
        result = mid
        right = mid - 1

print(result)
