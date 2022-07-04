# 1353 무한수열

import sys

m = sys.stdin.readline
n, p, q = map(int, m().split())

a_list = {0: 1, 1: 2}

def func(n, p, q):
    if n in a_list :
        return a_list[n]
    
    else:
        a_list[n] = func(n//p, p, q) + func(n//q, p, q)
        return a_list[n]

print(func(n, p, q))
