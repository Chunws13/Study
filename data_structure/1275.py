# 1275
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

info = list(map(int, input().split()))
order = [list(map(int, input().split())) for _ in range(m)]
table = [0] * n * 4

def init(start, end, idx):
    if start == end:
        table[idx] = info[start]
        return table[idx]
    
    mid = (start + end) // 2
    table[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx*2 + 1)
    return table[idx]

def calc(start, end, idx, left, right):
    if left <= start and end <= right:
        return table[idx]
    
    if end < left or start > right:
        return 0
    
    mid = (start + end) // 2
    return calc(start, mid, idx*2, left, right) + calc(mid + 1, end, idx*2 + 1, left, right)

def update(start, end, idx, point, value):
    if point < start or point > end:
        return
    
    if start == end:
        table[idx] = value
        return
    
    mid = (start + end) // 2
    update(start, mid, idx * 2, point, value)
    update(mid + 1, end, idx * 2 + 1, point, value)
    table[idx] = table[idx*2] + table[idx *2 + 1]

init(0, n-1, 1)

for left, right, point, value in order:
    left, right = min(left, right), max(left, right)
    print(calc(0, n-1, 1, left-1, right-1))
    update(0, n-1, 1, point-1, value)
