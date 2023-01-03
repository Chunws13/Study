# 14725
import sys
input = sys.stdin.readline

num = int(input())
floor = {"start": {}}

for _ in range(num):
    info = list(map(str, input().split()))
    
    point = floor['start']
    for i in range(1, len(info)):
        point[info[i]] = point.get(info[i], {})
        point = point[info[i]]

def printer(i, count):
    for f in sorted(i.keys()):
        print('--'*count, f, sep='')
        new_i = i[f]
        printer(new_i, count + 1)

printer(floor['start'], 0)
