import sys
m = sys.stdin.readline

size = int(m())
numbers = list(map(int, m().split(' ')))
answer = [0] * size

for i in range(size):
    tmp = 0
    for j in range(i):
        if numbers[i] > numbers[j]:
            tmp = max(answer[j], tmp)
        
    answer[i] = tmp + 1

print(max(answer))
