import sys

m = sys.stdin.readline

total = int(m())
plus_list, minus_list = [], []
answer = 0

# 양수 / 음수 나누기
for i in range(total):
    number = int(m())
    if number > 0:
        plus_list.append(number)
    
    else:
        minus_list.append(number)

minus_list.sort(reverse=True)
plus_list.sort()

# 리스트 별 계산
for num_list in [minus_list, plus_list]:
    while num_list:
        n = num_list.pop()
        if num_list and num_list[-1] * n > n:
            m = num_list.pop()
            answer += n*m
        
        else:
            answer += n

print(answer)