# 10868
import sys, math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

info = [int(input()) for _ in range(n)]
order = [list(map(int, input().split())) for _ in range(m)]

table = [0] * n * 4

def setting(start, end, idx):
    if start == end:
        table[idx] = info[start]
        return table[idx]
    
    mid = (start + end) // 2
    table[idx] = min(setting(start, mid, idx * 2), setting(mid + 1, end, idx*2 + 1))
    return table[idx]

def find(start, end, idx, left, right):
    if left <= start and end <= right:
        return table[idx]
    
    if end < left or start > right:
        return math.inf
    
    mid = (start + end) // 2
    return min(find(start, mid, idx*2, left, right), find(mid + 1, end, idx*2 + 1, left, right))

setting(0, n-1, 1)
for left, right in order:
    print(find(0, n-1, 1, left-1, right-1))
