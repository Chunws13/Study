# 강의실
import sys
import heapq

m = sys.stdin.readline

class_num = int(m())
info = [list(map(int, m().split())) for _ in range(class_num)]

start, end = [], []

# 시작 시간 순으로 정렬
for i in info:
    n, s, e = map(int, i)
    heapq.heappush(start, [s, e])

# 시작 시간 정령은 보장, 일찍 끝나는 시간 기준으로 등록
# 시작 시간이 가장 일찍 끝나는 시간보다 뒤라면, 강의실을 쓸 수 있으므로, 강의시 배정 정보를 교체
# 그렇지 않다면 - 시작 시간이 가장 빨리 끝나는 시간보다 뒤라면 - 정보 추가 
while start:
    s, e = heapq.heappop(start)
    if len(end) == 0:
        heapq.heappush(end, [e, s])
    
    elif s >= end[0][0]:
        heapq.heappop(end)
        heapq.heappush(end, [e, s])
    
    else:
        heapq.heappush(end, [e, s])

print(len(end))
