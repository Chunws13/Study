import sys
input = sys.stdin.readline

a = [''] + list(map(str, input().strip()))
b = [''] + list(map(str, input().strip()))
c = [''] + list(map(str, input().strip()))


table = [[[0] * len(c) for _ in range(len(b))] for _ in range(len(a))]

    
for i in range(1, len(a)):
    for j in range(1, len(b)):
        for k in range(1, len(c)):
            if a[i] == b[j] == c[k]:
                table[i][j][k] = table[i-1][j-1][k-1] + 1
            
            else:
                table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k], table[i][j][k-1])
for t in table:
    print(t)

print(table[-1][-1])
