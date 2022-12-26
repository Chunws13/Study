# 1039
import sys, copy
from collections import deque
input = sys.stdin.readline

number, chance = map(int, input().split())
start = deque([[number, 0]])
answer = -1
visited = []
while start:
    n, c = start.popleft()
    if c == chance:
        answer = max(answer, n)
    
    elif c < chance:
        origin_value = list(map(int, str(n)))
        start_value, tmp_list = origin_value[0], []
        for i in range(len(origin_value) - 1):
            for j in range(i + 1, len(origin_value)):
                if i == 0 and origin_value[j] == 0:
                    continue
                
                tmp_n = copy.deepcopy(origin_value)
                tmp_n[i], tmp_n[j] = tmp_n[j], tmp_n[i]
                tmp_n_sum = sum([num * (10 ** idx) for idx, num in enumerate(tmp_n[::-1])])
                
                if tmp_n_sum + c + 1 not in visited:
                    visited.append(tmp_n_sum + c + 1)
                    start.append([tmp_n_sum, c + 1])
                        
print(answer)
