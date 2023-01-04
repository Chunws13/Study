# 12015
import sys
input = sys.stdin.readline

num = int(input())
info = list(map(int, input().split()))

answer = []
for i in info:
    if len(answer) == 0 or i > answer[-1]:
        answer.append(i)
    
    else:
        left, right = 0, len(answer)-1
        while left <= right:
            mid = (left + right) // 2
            if answer[mid] == i:
                left = mid
                break
            
            elif answer[mid] < i:
                left = mid + 1
            
            else:
                right = mid - 1
        
        answer[left] = i
    print(answer)
print(len(answer))
