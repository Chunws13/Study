# 1005 위상정렬, DP ,그래프
import sys
from collections import deque
m = sys.stdin.readline

test_case = int(m())

for _ in range(test_case):
    b_num, b_rules = map(int, m().split(' '))
    b_times = [0] + list(map(int, m().split(' ')))

    build = [[] for _ in range(b_num + 1)]
    order, answer = [0] * (b_num + 1), [0] * (b_num + 1)
    for r in range(b_rules):
        a, b = map(int, m().split(' '))
        build[a] += [b]
        order[b] += 1

    target = int(m())
    start = deque()
    
    for o in range(1, b_num+1):
        if order[o] == 0:
            start.append(o)
            answer[o] = b_times[o]

    while start:
        s = start.popleft()
        for i in build[s]:
            answer[i] = max(answer[s] + b_times[i], answer[i])
            order[i] -= 1
            if order[i] == 0:
                start.append(i)
    
    print(answer[target])
