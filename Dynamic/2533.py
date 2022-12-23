# 2533
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

people = int(input())
network = [[] for _ in range(people + 1)]

for i in range(people-1):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

checker = [0] * (people + 1)

def slove(me, friend):
    f_list = []
    if len(network[me]) == 1 and network[me] == [friend]:
        checker[friend] = 1
                    
    else:
        for n in network[me]:
            if n == friend:
                continue
            slove(n, me)
            f_list.append(checker[n])
            
        if min(f_list) == 0:
            checker[me] = 1
        

slove(1, 1)
print(sum(checker))
