import sys
input = sys.stdin.readline

case = int(input())

answers = []
tmp = []
for _ in range(case):
    number = int(input())
    info = sorted([input().strip() for _ in range(number)])
    
    status = True
    for i in range(number - 1):
        if info[i] == info[i+1][:len(info[i])]:
            status = False
            break
    
    if status:
        answers.append("YES")
    
    else:
        answers.append("NO")
    
for answer in answers:
    print(answer)
