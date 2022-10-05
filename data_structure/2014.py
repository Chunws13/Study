from email import header
import sys
import heapq
m = sys.stdin.readline

n, t = map(int, m().split())
info = list(map(int, m().split()))

m_value = 0
answer, start, visited = [], [1], set()

while len(answer) <= t:
    s = heapq.heappop(start)
    answer.append(s)
    
    for i in info:
        new_value = i * s
        if len(start) >= t and new_value >= m_value:
            continue
        if new_value not in visited:
            visited.add(new_value)
            m_value = max(m_value, new_value)
            heapq.heappush(start, new_value)

print(answer[-1])
