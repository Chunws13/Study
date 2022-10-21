import sys
m = sys.stdin.readline

a = [' '] + list(map(str, m().strip()))
b = [' '] + list(map(str, m().strip()))

answer = [[""] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            answer[i][j] = answer[i-1][j-1] + a[i]
        
        elif len(answer[i-1][j]) > len(answer[i][j-1]) :
            answer[i][j] = answer[i-1][j]
        
        else:
            answer[i][j] = answer[i][j-1]

print(len(answer[-1][-1]))
print("".join(answer[-1][-1]))
