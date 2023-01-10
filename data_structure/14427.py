# 14427
import sys, math
input = sys.stdin.readline

size = int(input())
ini = list(map(int, input().split()))
info = {idx + 1: num for idx, num in enumerate(ini)}

table = [0] * len(info) * 4
query = int(input())

def init(start, end, index):
    if start == end:
        table[index] = start
        return table[index]
    
    mid = (start + end) // 2
    left, right = init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1)
    
    if info[left] > info[right]:
        table[index] = right
    else:
        table[index] = left
        
    return table[index]
    
def change(start, end, index, point):
    if start > point or end < point:
        return table[index]
    
    if start == end:
        return table[index]
    
    mid = (start + end) // 2
    left = change(start, mid, index * 2, point)
    right = change(mid+1, end, index * 2 + 1, point)
    
    if info[left] > info[right]:
        table[index] = right
    
    else:
        table[index] = left
        
    return table[index]
    
init(1, size, 1)
for _ in range(query):
    order = list(map(int, input().split()))
    if order[0] == 2:
        print(table[1])
    
    else:
        info[order[1]] = order[2]
        change(1, size, 1, order[1])
