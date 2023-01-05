# 11505
import sys, math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())

info = [int(input()) for _ in range(n)]
order = [list(map(int, input().split())) for _ in range(m + k)]
mod = 1000000007
table = [0] * n * 4

def init(start, end, idx):
    if start == end:
        table[idx] = info[start]
        return table[idx] % mod
    
    mid = (start + end) // 2
    table[idx] = init(start, mid, idx * 2) * init(mid + 1, end, idx*2 + 1)
    return table[idx] % mod

def calc(start, end, idx, left, right):
    if left <= start and end <= right:
        return table[idx] % mod
    
    if end < left or start > right:
        return 1
    
    mid = (start + end) // 2
    return calc(start, mid, idx*2, left, right) * calc(mid + 1, end, idx*2 + 1, left, right)

def update(start, end, idx, point, value): # 차이값을 보내면 소수점 이하 발생 가능성, 변동값을 변동위치로 저장하고 재계산
    if point < start or point > end:
        return
    
    if start == end:
        table[idx] = value
        return
    
    mid = (start + end) // 2
    update(start, mid, idx * 2, point, value)
    update(mid + 1, end, idx * 2 + 1, point, value)
    table[idx] = table[idx*2] * table[idx *2 + 1] % mod

init(0, n-1, 1)
for option, left, right in order:
    if option == 1:
        update(0, n-1, 1, left-1, right)
        info[left-1] = right
        
        
    else:
        print(calc(0, n-1, 1, left-1, right-1) % mod)
