# 3665
import sys
input = sys.stdin.readline

case = int(input())
for _ in range(case):
    teams = int(input())
    origin = list(map(int, input().split()))
    checker = [0] * (teams + 1)
    
    change_info = {t : origin[rank + 1:] for rank, t in enumerate(origin)}
    origin_rank = {t : rank + 1 for rank, t in enumerate(origin)}
    for rank, t in enumerate(origin):
        checker[t] = rank
    
    c_num = int(input())
    for _ in range(c_num):
        a, b = map(int, input().split())
        if origin_rank[a] < origin_rank[b]:
            change_info[a].remove(b)
            change_info[b] += [a]
            checker[a] += 1
            checker[b] -= 1
        
        else:
            change_info[b].remove(a)
            change_info[a] += [b]
            checker[b] += 1
            checker[a] -= 1
    
    answer, qeue = [], []
    for o in origin[::-1]:
        if checker[o] == 0:
            qeue.append(o)
    
    status = False
    if len(qeue) >= 2:
        print('?')
        break
    
    for _ in range(teams):
        if len(qeue) == 0:
            status = True
            break
        
        q = qeue.pop()
        for c in change_info[q]:
            checker[c] -= 1
            if checker[c] == 0:
                qeue.append(c)
        
        answer.append(q)
    
    if status:
        print("IMPOSSIBLE")
    
    else:
        print(' '.join(map(str, answer)))
