import sys
import heapq
m = sys.stdin.readline

problem, num = map(int, m().split())
info = [list(map(int, m().split())) for _ in range(num)]

p_info = [0] * (problem + 1)
before_do = [[] for i in range(problem+1)]

# 선행 학습 요소 넣기
for i in info:
    be, af = i[0], i[1]
    p_info[af] += 1
    before_do[be] += [af]

start, answer = [], []

# 선행 학습 필요 없는 값 부터 시작
for p in range(1, problem + 1):
    if p_info[p] == 0:
        start.append(p)

while start:
    s = heapq.heappop(start)
    for s1 in before_do[s]:
        p_info[s1] -=1
        if p_info[s1] == 0:
            heapq.heappush(start, s1)
    answer.append(s)

print(" ".join(map(str, answer)))
