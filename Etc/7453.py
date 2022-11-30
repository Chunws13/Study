# 7453
import sys
input = sys.stdin.readline

list_len = int(input())

a, b, c, d = [], [], [], []
for _ in range(list_len):
    a1, b1, c1, d1 = map(int, input().split())
    a += [a1]
    b += [b1]
    c += [c1]
    d += [d1]

a.sort()
b.sort()
c.sort()
d.sort()

ab, cd = {}, {}
for i in range(list_len):
    for j in range(list_len):
        try:
            ab[a[i] + b[j]] += 1
        except:
            ab[a[i] + b[j]] = 1

answer = 0

for i in range(list_len):
    for j in range(list_len):
        try:
            answer += ab[-(c[i] + d[j])]
        
        except:
            pass
        

print(answer)
