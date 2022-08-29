# 멀티탭 스케줄링
import sys
from collections import deque
m = sys.stdin.readline

count, use = map(int, m().split())
name = deque(map(int, m().split()))

answer, result = [], 0
while name:
    n = name.popleft()
    if n in answer:
        continue
    
    if len(answer) == count:
        idx, number = 0, 0
        for a in answer:
            if a not in name: # 잔여 사용 횟수 없음
                idx = answer.index(a)
                break
            else: # 사용 회수 있음 - 제일 늦게 나오는 번호
                if name.index(a) > number:
                    idx = answer.index(a)
                    number = name.index(a)
        answer.pop(idx)
        result += 1
    
    answer.append(n)
    
print(result)
