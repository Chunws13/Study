import sys
input = sys.stdin.readline

n, m = map(int, input().split())
play = list(map(int, input().split()))

left, right = 0, max(play) * n
t = 0
if n <= m:
    print(n)

else:
    while left <= right:
        mid = (left + right) // 2
        cnt = m

        for p in play:
            cnt += mid // p

        if cnt >= n:
            t = mid
            right = mid - 1

        else:
            left = mid + 1
    
    cnt = m
    for i in range(m):
        cnt += (t-1) // play[i]

    for i in range(m):
        if t % play[i] == 0:
            cnt += 1
        
        if cnt == n:
            break
    print(i+1)
