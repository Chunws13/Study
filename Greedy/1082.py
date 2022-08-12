# 방 번호 만들기
import sys
m = sys.stdin.readline

number = int(m())
cost = list(map(int, m().split()))
limit = int(m())

# 최대 개수
answer = []
h_cost, h_number, t_cost, t_number = 51, 0, 51, 0

for i in range(len(cost)):
    if t_cost > cost[i]:
        t_number = i
        t_cost = cost[i]
    
    if i > 0 and h_cost >= cost[i]:
        h_number = i
        h_cost = cost[i]
        
if h_number == t_number != 0: # 둘 최소 번호가 같음 = 최소값이 0이 아님
    div = limit // h_cost
    answer = [h_number] * div
    mod = limit % h_cost

elif limit >= h_cost:  # 둘이 다르지만, 0 제외 최소값 한도 내
    div = (limit - h_cost) // t_cost # 0 제외 최소값을 뺀 몫
    answer = [h_number] + [t_number] * div
    mod = (limit - h_cost) % t_cost

else: 
    print(0)
    sys.exit()


for a in range(len(answer)):
    start = answer[a]
    
    for s in range(start+1, len(cost)):
        if mod + cost[start] >= cost[s]:
            answer[a] = s
            mod += cost[start] - cost[s]
            start = s

print(int("".join(map(str, answer))))
