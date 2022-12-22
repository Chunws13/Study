# 7579
import sys, math
input = sys.stdin.readline

number, need = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

INF = math.inf
min_value = INF
info = {} 

for i in range(number):
    if memory[i] >= need:
        min_value = min(min_value, cost[i])
        continue
    
    tmp_dic = {cost[i] : memory[i]}
    
    for j in info:
        new_memory, new_cost = memory[i] + info[j], cost[i] + j
        if new_memory >= need:
            min_value = min(min_value, new_cost)
            continue
        
        tmp_dic[new_cost] = new_memory
        
    for k in tmp_dic:
        info[k] = max(info.get(k, 0), tmp_dic[k])

print(min_value)
