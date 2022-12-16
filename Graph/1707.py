# 1707
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

case = int(input())

def check(now):
    if visited[now] == -1:
        visited[now] = 1
        
    for n in node_info[now]:
        if visited[n] == visited[now]:
            return False
        
        if visited[n] == -1:
            visited[n] = (visited[now] + 1) % 2
            check(n)
    
    return True

result = []
for _ in range(case):
    v, e = map(int, input().split())
    node_info = [[] for _ in range(v + 1)]
    
    for _ in range(e):
        a, b = map(int, input().split())
        node_info[a] += [b]
        node_info[b] += [a]
        
    visited = [-1] * (v + 1)
    status = True
    for i in range(1, v+1):
        if check(i) == False:
            status = False
            break
    
    if status:
        print("YES")
    
    else:
        print("NO")
