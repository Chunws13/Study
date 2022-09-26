import sys
from typing import OrderedDict
m = sys.stdin.readline

number, change, sum_num = map(int, m().split())

num_info = [int(m()) for _ in range(number)]
order_info = [list(map(int, m().split())) for _ in range(change+sum_num)]

tree = [0] * number * 4

def c_tree(start, end, idx):
    if start == end:
        tree[idx] = num_info[start]
        return tree[idx]
    
    mid_p = (start + end) // 2
    tree[idx] = c_tree(start, mid_p, idx*2) + c_tree(mid_p+1, end, idx*2+1)
    return tree[idx]

def sum_tree(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and right >= end:
        return tree[idx]
    
    mid = (start + end) // 2
    return sum_tree(start, mid, idx * 2, left, right) + sum_tree(mid+1, end , idx * 2 + 1, left, right)

def update_tree(start, end, idx, target, adj_num):
    if target < start or target > end:
        return
    
    tree[idx] += adj_num
    
    if start == end:
        return
    
    mid = (start + end) // 2
    update_tree(start, mid, idx*2, target, adj_num)
    update_tree(mid+1, end, idx*2 + 1, target, adj_num)

c_tree(0, number-1, 1)
answer = []
for o in order_info:
    order, a, b = o[0], o[1], o[2]
    
    if order == 1:
        adj_num = b - num_info[a-1]
        num_info[a-1] = b
        update_tree(0, number-1, 1, a-1, adj_num)
        
    else:
        answer.append(sum_tree(0, number-1, 1, a-1, b-1))
        
print(*answer, sep='\n')
