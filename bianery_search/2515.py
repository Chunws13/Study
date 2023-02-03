import sys
input = sys.stdin.readline

n, s = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(n)]
info.sort(key=lambda x:(x[0], -x[1]))

answer = [0] * n

for i in range(n):
    if i == 0 : # 첫 그림은 전시하는 것으로 가정
        answer[i] = info[i][1]
        continue

    value = 0
    left, right = 0, i-1
    while left <= right: # 이전까지 그림들을 이분 탐색하면서
        mid = (left + right) // 2

        if info[i][0] - info[mid][0] < s: # 그림 높이가 기준 높이 미만이면 우측 한도 줄이고
            right = mid - 1
        
        else: # 기준 높이 이상이면 좌측 한도 높이면서, 최대값 저장
            value = max(value, answer[mid])
            left = mid + 1
            
    answer[i] = max(answer[i-1], value + info[i][1]) # 직전 최대값과 비교해서 업데이트
        
print(answer[-1])
