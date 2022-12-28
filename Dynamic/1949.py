# 1949
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

city = int(input())
link_info = [[] for _ in range(city+1)]
people = [0] + list(map(int, input().split()))

for _ in range(city-1):
    a, b = map(int, input().split())
    link_info[a].append(b)
    link_info[b].append(a)
    

def check(here):
    visited[here] = 1
    for n in link_info[here]:
        if visited[n]:
            continue
        
        check(n)
        answer[here][0] += answer[n][1]
        answer[here][1] += max(answer[n][0], answer[n][1])
        
answer = [[people[i], 0] for i in range(city+1)]
visited = [0] * (city+1)
check(1)
print(max(answer[1]))
