# 11866
import sys
m = sys.stdin.readline

n, k = map(int, m().split())
info = [i +1 for i in range(n)]
answer = []

idx = 0
while len(info):
    idx = (idx + k-1) % len(info)
    answer.append(info[idx])
    info = info[:idx] + info[idx+1:]

print("<",end="")
print(", ".join(map(str,answer)),end="")
print(">")
