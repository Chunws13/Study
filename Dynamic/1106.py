# 1106 호텔, 최소비용

import sys
import math

m = sys.stdin.readline

target, city = map(int, m().split(' '))
info = []
INF = math.inf

for i in range(city):
    a, b = map(int, m().split(' '))
    info.append([a, b])

answer = [0] + [INF] * (target + 101)

info.sort(key=lambda x:x[1])

for c, p in info:
    for k in range(p, len(answer)):
        answer[k] = min(answer[k - p] + c, answer[k])
        
print(min(answer[target:]))
