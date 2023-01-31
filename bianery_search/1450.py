# 1450
import sys
from itertools import combinations
input = sys.stdin.readline

n, c = map(int, input().split())
info = list(map(int, input().split()))

left, right = info[:n//2], info[n//2:]
sum_left, sum_right = [], []

for i in range(1, len(left) + 1):
    comb = combinations(left, i)
    for co in comb:
        sum_left.append(sum(co))

for i in range(1, len(right) + 1):
    comb = combinations(right, i)
    for co in comb:
        sum_right.append(sum(co))

sum_left.sort()
sum_right.sort()

result = 1
for l in sum_left:
    if l <= c:
        result += 1

for r in sum_right:
    if r <= c:
        result += 1

lp, rp = 0, len(sum_right) - 1
for l in sum_left:
    lp, rp = 0, len(sum_right) - 1
    while lp <= rp:
        mid = (lp + rp) // 2
        number = l + sum_right[mid]
        if number <= c:
            lp = mid + 1
        
        else:
            rp = mid - 1
    
    result += lp

print(result)
