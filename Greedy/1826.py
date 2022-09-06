import sys
from collections import deque
m = sys.stdin.readline

station = int(m())
info = deque(sorted([list(map(int, m().split())) for _ in range(station)]))
info.append(list(map(int, m().split())))

fuel = info[-1][-1]
spare = []
answer, now = 0, 0

while info:
    i = info.popleft()
    # 연료양이 부족하면 이전 주유소에서 주유한 것으로 간주
    while i[0] - now > fuel:
        try:
            s = spare.pop()
            fuel += s[1]
            answer += 1

        except: # 이전 주유소에 모두 들렀어도 불가능한 경우 -1 출력
            print(-1)
            sys.exit()
    
    spare.append(i)
    spare.sort(key=lambda x: x[1])
    
    fuel -= (i[0] - now)
    now = i[0]

print(answer)
