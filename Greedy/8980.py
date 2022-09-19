import sys
m = sys.stdin.readline

num, limit = map(int, m().split())
box = int(m())
info = sorted([list(map(int, m().split())) for _ in range(box)],key = lambda x:x[1])

answer = 0
truck = [limit] * (num + 1)

for i in info:
    tmp = limit
    # 출발지부터 목적지 이전까지 선적 가능한 택배의 양 (최소)
    for j in range(i[0], i[1]):
        tmp = min(tmp, truck[j])
    
    # 선적 가능한 양과 옮겨야 하는 택배 수 비교
    tmp = min(tmp, i[2])
    
    # 경로 사이의 선적 가능한 택배의 양 줄이기
    for k in range(i[0], i[1]):
        truck[k] -= tmp
    
    # 줄인 수 만큼은 옮길 수 있음
    answer += tmp

print(answer)
