# 카잉달력

import sys
from math import gcd

m = sys.stdin.readline

def sol(x, y):
    return x * y // gcd(x, y)

case = int(m())
input_case, answer_list = [], []

for _ in range(case):
    input_case.append(list(map(int, m().split(' '))))

for a in input_case:
    m, n, x, y = a[0], a[1], a[2], a[3]
    
    find = False
    for k in range(x, sol(m, n) + 1, m):
        
        j = k % n
        if j == 0:
            j += n
        
        if  j == y:
            answer_list.append(k)
            find = True
            break
    
    if find == False:
        answer_list.append(-1)

for an in answer_list:
    print(an)
