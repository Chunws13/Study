# 20040
import sys

m = sys.stdin.readline
point, game = map(int, m().split())
info = [list(map(int, m().split())) for _ in range(game)]
node = [i for i in range(point)]

def find(x):
    if node[x] == x:
        return x
    return find(node[x])

def union(x, y):
    new_x, new_y = find(x), find(y)
    if new_x < new_y:
        node[new_y] = new_x
    
    else:
        node[new_x] = new_y

for i in range(game):
    a, b = info[i][0], info[i][1]
    new_a, new_b = find(a), find(b)
    if new_a == new_b:
        print(i+1)
        sys.exit()
    
    else:
        union(a, b)

print(0)
