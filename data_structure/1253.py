# 1253
import sys
input = sys.stdin.readline

n = int(input())
info = sorted(list(map(int, input().split())))

answer = 0

for i in range(n):
    point = info[i]
    tmp_list = info[:i] + info[i+1:]
    left, right = 0, n-2
    
    while left < right:
        number = tmp_list[left] + tmp_list[right]
        
        if number == point:
            answer += 1
            break
        
        elif number > point:
            right -= 1
        
        else:
            left += 1
    
print(answer)
