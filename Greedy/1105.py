# 팔
import sys
m = sys.stdin.readline

left, right = map(str, m().split())
answer = 0

if len(left) != len(right):
    answer = 0

else:
    for info in zip(left, right):
        if info[0] == info[1] and info[0] == '8':
            answer += 1
        
        elif info[0] == info[1]:
            continue

        else:
            break
print(answer)