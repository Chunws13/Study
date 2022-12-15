# 12904
import sys
input = sys.stdin.readline

start, target = str(input().strip()), str(input().strip())

status = 0

def checker(word):
    global status
    if len(word) == len(start):
        if word == start:
            status = 1
            return
        
    if len(word) > len(start):
        if word[-1] == 'A':
            checker(word[:-1])
        
        else:
            checker(word[:-1][::-1])

checker(target)
print(status)
