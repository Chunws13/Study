# 2213
import sys
input = sys.stdin.readline

size = int(input())
info = [0] + list(map(int, input().split()))
visited = [0] * (size + 1)
answer = [[info[i], 0] for i in range(size + 1)]
node = [[] for _ in range(size + 1)]

for _ in range(size-1):
    a, b = map(int, input().split())
    node[a] += [b]
    node[b] += [a]

def chceker(here):
    visited[here] = 1
    for h in node[here]:
        if visited[h] == 0:
            chceker(h)
            answer[here][0] += answer[h][1] # 해당 노드 포함
            answer[here][1] += max(answer[h][0], answer[h][1]) # 해당 노드 미포함

chceker(1)
print(max(answer[1]))
answer_list = []
for i in range(1, size +1): # 노드 포함하는 값이 더 높을 때
    status = True
    
    if answer[i][0] > answer[i][1]: # 나랑 연결된 정점이 answer_list에 없어야 함
        for j in node[i]:
            if j in answer_list:
                status = False
                break
        if status:
            answer_list.append(i)

print(' '.join(map(str, answer_list)))
