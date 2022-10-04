# 17298
import sys
from collections import deque
m = sys.stdin.readline

size, need = map(int, m().split())
n_pop = deque(map(int, m().split()))
num_list = deque([i+1 for i in range(size)])

answer, now = 0, 1
while n_pop:
    n = n_pop.popleft()
    while n != 1:
        # 좌측 이동
        if n-1 <= len(num_list) // 2:
            num_list.append(num_list.popleft())
            n = n - 1 if n > 1 else len(num_list)
            for i in range(len(n_pop)):
                n_pop[i] = n_pop[i] -1 if n_pop[i] > 1 else len(num_list)
        else:
            num_list.appendleft(num_list.pop())
            n = n + 1 if n < len(num_list) else 1
            for i in range(len(n_pop)):
                n_pop[i] = n_pop[i] + 1 if n_pop[i] < len(num_list) else 1
        answer += 1
        # if answer > 10:
        #     break
    num_list.popleft()
    for i in range(len(n_pop)):
        n_pop[i] = n_pop[i] -1 if n_pop[i] > 1 else len(num_list)
print(answer)
