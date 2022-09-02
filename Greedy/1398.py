import sys
m = sys.stdin.readline

case = int(m())

def soultion(number, coin):
    answer = 0
    while number:
        target = number % 100
        tmp_list = [i for i in range(target+1)]
        
        for c in coin:
            for t in range(target+1):
                if t >= c:
                    tmp_list[t] = min(tmp_list[t], tmp_list[t-c] + 1)
        answer += tmp_list[target]
        number //= 100
    return answer
    
for _ in range(case):
    money = int(m())
    coin = [10, 25]
    print(soultion(money, coin))
