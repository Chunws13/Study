import sys
input = sys.stdin.readline

size = int(input())
chess = [0] * size
answer = 0

def check(x):
    for i in range(x):
        if chess[x] == chess[i]:
            return False
        
        if abs(chess[x] - chess[i]) == x - i:
            return False
    return True

def queen(x):
    global answer
    if x == size:
        answer += 1
        return
    
    else:
        for i in range(size):
            chess[x] = i
            if check(x):
                queen(x + 1)

queen(0)
print(answer)
