# 1354번 등비수열2

import sys

m = sys.stdin.readline
n, p, q, x, y = map(int, m().split())

a_list = {}

def func(n):
    global p, q, x, y

    if n <= 0:
        return 1
    
    elif n in a_list :
        return a_list[n]
    
    else:
        a_list[n] = func(n//p - x) + func(n//q - y)
        return a_list[n]

print(func(n))
