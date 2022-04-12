# 신입 사원 선발
import sys

m = sys.stdin.readline

case = int(m())
answer = []

for c in range(case):
    candidate = []
    num = int(m())
    plus = 1

    for _ in range(num):
        candidate.append(list(map(int, m().split())))
    
    candidate.sort()
    
    # 1등의 2번 등수
    standard = candidate[0][1]
    
    for c in candidate:
        # 2번 등수 높다 = 1개 부분이라도 순위 더 높음
        # 새로운 기준점
        if c[1] < standard:
            standard = c[1]
            plus += 1

    answer.append(plus)

for a in answer:
    print(a)