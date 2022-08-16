import sys
import heapq
m = sys.stdin.readline

number = int(m())
n_list = list(map(int, m().split()))

n_list.sort()
answer, result = [], 0

while n_list:
    n = n_list.pop()
    while len(answer) >= 2 and answer[0] <= answer[-1] - n: 
        heapq.heappop(answer)
    heapq.heappush(answer, -n)
    result = max(len(answer), result)

print(result)
