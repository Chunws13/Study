# 트리 순회
import sys
m = sys.stdin.readline

class Tree:
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;

def pre(node):
    print(node.data, end= '')
    if node.left != '.': pre(node.left)
    if node.right != '.': pre(node.right)

def inorder(node):
    if node.left != '.': inorder(node.left)        
    print(node.data, end='')
    if node.right != '.': inorder(node.right)

def back(node):
    if node.left != '.' : back(node.left)
    if node.right != '.': back(node.right)
    print(node.data, end='')

size = int(m())
answer = []
for i in range(size):
    d = m().split()
    T = Tree(d[0])
    
    T.left = d[1]
    T.right = d[2]
    answer.append(T)

for i in range(size):
    for j in range(size):
        if answer[i].data == answer[j].left:
            answer[j].left = answer[i]
        
        elif answer[i].data == answer[j].right:
            answer[j].right = answer[i]

pre(answer[0])
print()
inorder(answer[0])
print()
back(answer[0])
