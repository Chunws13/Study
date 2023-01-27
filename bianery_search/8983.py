import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())

point = list(map(int, input().split()))
point.sort()

target = []
for _ in range(n):
    target.append(list(map(int, input().split())))

result = 0

# 사냥감을 기준으로 하는 경우, 정렬 구상이 용이
for x, y in target:
    left, right = 0, m-1
    while left <= right:
        mid = (left + right) // 2
        r = abs(point[mid] -x ) +y
        if r <= l:
            result += 1
            break

        if point[mid] > x:
            right = mid - 1
        
        else:
            left = mid + 1
print(result)
