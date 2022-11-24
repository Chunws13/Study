import sys, math
input = sys.stdin.readline

god, link = map(int, input().split())
location = [list(map(int, input().split())) for _ in range(god)]
link_info = [list(map(int, input().split())) for _ in range(link)]

dis_info = []
parent = [i for i in range(god + 1)]

def get_distance(a, b):
    x, y = a[0] - b[0], a[1] - b[1]
    return math.sqrt(x**2 + y**2)

def find(t):
    if parent[t] != t:
      return find(parent[t])
    return t

def union(a, b):
    new_a, new_b = find(a), find(b)
    if new_a < new_b:
        parent[new_b] = new_a
    
    else:
        parent[new_a] = new_b

for i in range(god-1):
    for j in range(i+1, god):
        dis_info.append([i + 1, j + 1, get_distance(location[i], location[j])])

dis_info.sort(key=lambda x:x[2])
answer = 0

for x, y in link_info:
    union(x, y)

for f, t, distance in dis_info:
    if find(f) != find(t):
        answer += distance
        union(f, t)
        
print(format(answer, ".2f"))
