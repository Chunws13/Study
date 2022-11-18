# 2668
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(number, p):
    global info, visited, tmp
    visited[number] = 1
    for n in info[number]:
        if visited[n]:
            if n != p:
                return True
        
        else:
            if find(n, number):
                return True
            
    return False
    
result = []
case_no = 1
while True:
    tree, node = map(int, input().split())
    info = [[] for _ in range(tree+1)]
    visited = [0] * (tree + 1)
    tmp = 0
    if tree == 0 and node == 0:
        break
    
    for _ in range(node):
        a, b = map(int, input().split())
        info[a] += [b]
        info[b] += [a]

    for i in range(1, tree+1):
        if visited[i] == 0:
            if not find(i, 0):
                tmp += 1
    
    message = ''
    if tmp == 0:
        message = "Case {}: No trees.".format(case_no)
    
    elif tmp == 1:
        message = "Case {}: There is one tree.".format(case_no)
        
    else:
        message = "Case {}: A forest of {} trees.".format(case_no, tmp)
    result.append(message)
    case_no += 1
    
print('\n'.join(result))
