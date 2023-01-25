import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
info = list(map(int, input().split()))

# 수열 분해 
left, right = info[:n//2], info[n//2:]

left_sum, right_sum = [], []

# 좌,우 수열 부분합 계산
for i in range(1, len(left) + 1):
    com = combinations(left, i)
    for c in com:
        left_sum.append(sum(c))

for i in range(1, len(right) + 1):
    com = combinations(right, i)
    for c in com:
        right_sum.append(sum(c))

left_sum.sort()
right_sum.sort()
result = 0

# 좌,우 수열 내 정답 확인
for l in left_sum:
    if l == s:
        result += 1

for r in right_sum:
    if r == s:
        result += 1

lp, rp = 0, len(right_sum) - 1

# 포인터 범위 내
while lp < len(left_sum) and rp >= 0:
    number = left_sum[lp] + right_sum[rp]
    # 목표 값 있는 경우
    if number == s:
        save_lp, save_rp = lp, rp
        
        # 좌측 수열 동일 값 있는지 확인
        while save_lp < len(left_sum) and left_sum[save_lp] == left_sum[lp]:
            save_lp += 1
        
        # 우측 수열 동일 값 있는지 확인
        while save_rp >= 0 and right_sum[save_rp] == right_sum[rp]:
            save_rp -= 1
        
        # 중복 계산 제거
        result += (save_lp - lp) * (rp - save_rp)
        lp, rp = save_lp, save_rp

    elif number > s:
        rp -= 1
    
    else:
        lp += 1

print(result)
