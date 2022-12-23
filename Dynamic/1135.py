# 1135
import sys
input = sys.stdin.readline

people = int(input())
info = list(map(int, input().split()))
company = [[] for _ in range(people)]

if people == 1: # 자기 자신뿐이라면 전달에 시간 소요 X
    print(0)
    sys.exit()
    
for i in range(1, people):
    company[info[i]].append(i)

time_table = [0] * people

def slove(me, boss):
    tmp_list = []
    if company[me]:
        for i in company[me]:
            slove(i, me)
            tmp_list.append(time_table[i])
    
    else:
        time_table[boss] += 1
    
    tmp_list.sort(reverse = True)
    for number, time_flow in enumerate(tmp_list):
        time_table[me] = max(time_table[me], time_flow + number + 1)

slove(0, 0)
print(time_table[0])
