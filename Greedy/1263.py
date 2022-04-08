#1263
import sys
m = sys.stdin.readline

number = int(m())

s = []
for _ in range(number):
    s.append(list(map(int, m().split())))

s.sort(key=lambda x:x[1])
while len(s) != 1:
    last = s.pop()
    last_f = last[1] - last[0]
    if s[-1][1] > last_f:
        s[-1][1] = last_f

answer = s[0][1] - s[0][0]

if answer >= 0:
    print(answer)
else:
    print(-1)