# 9466
import sys
m = sys.stdin.readline
sys.setrecursionlimit(10**6)

case = int(m())

def solve(number, h_list):
    global visited, people, check, answer
    
    visited[number] = 1
    next = h_list[number]
    
    if visited[next] == 0:
        solve(next, h_list)
    
    else:
        if check[next] == 0:
            answer += 1
            while number != next:
                next = h_list[next]
                answer += 1
            
    check[number] = 1
    
result = []
for _ in range(case):
    people, answer = int(m()), 0
    hope = [0] + list(map(int, m().split()))
    visited, check = [0] * len(hope), [0] * len(hope)
    
    for p in range(1, people + 1):
        if visited[p] == 0:
            solve(p, hope)
    
    result.append(people - answer)

for r in result:
    print(r)
