import sys
m = sys.stdin.readline

limit, size = map(int, m().split())
info = [i for i in range(limit+1)]

order_info = [list(map(int, m().split())) for _ in range(size)]

answer = []
# 부모가 자기 자신이 나올 때 까지 부모 노드로 올라감
def check(num):
    while num != info[num]:
        num = info[num]
    return num

# 부모 숫자를 검색한 후, 더 낮은 수를 가진 부모의 새로운 부모로 더 높은 수를 선택
def union(a, b):
    new_a, new_b = check(a), check(b)
    if new_a > new_b:
        info[new_b] = new_a
    else:
        info[new_a] = new_b

for o in order_info:
    order, a, b = o[0], o[1], o[2]
    
    if order == 0:
        union(a, b)
    
    if order == 1:
        if check(a) == check(b):
            answer.append("YES")
        
        else:
            answer.append("NO")

for a in answer:
    print(a)
print(info)
