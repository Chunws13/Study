# 문자열 뒤집기

import sys
import string

m = sys.stdin.readline
index = list(string.ascii_uppercase)

target = list(map(str, m().strip()))

for t in range(len(target)-1):
    if index.index(target[t]) < index.index(target[t+1]):
        target = target[t::-1] + target[t+1:]

        target = target[t+1::-1] + target[t+2:]


print("".join(target[::-1]))
