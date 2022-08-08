# 수 묶기
import sys
m = sys.stdin.readline

num = int(m())
n_list = [int(m().strip()) for i in range(num)]

plus, minus = [], []

while n_list:
    n = n_list.pop()
    if n > 0:
        plus.append(n)
    else:
        minus.append(n)

plus.sort()
minus.sort(reverse=True)

answer = 0
while plus:
    p = plus.pop()
    if plus:
        p1 = plus.pop()
        answer += max(p * p1, p + p1)
    
    else:
        answer += p

while minus:
    m = minus.pop()
    if minus:
        answer += m * minus.pop()
    else:
        answer += m

print(answer)
