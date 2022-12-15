# 11049
import sys
input = sys.stdin.readline

size = int(input())
info = [list(map(int , input().split())) for _ in range(size)]
table = [[[0, []]] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if i == j:
            table[i][j] = [0, info[i]]
        
for i in range(size):
    for j in range(i - 1, -1, -1):
        table_size = [info[j][0] , info[i][1]]
        min_value = 2**31 -1
        k = 0
        while k + j < i:
            min_value = min((table[j][j + k][0] + table[j + k + 1][i][0]) + table[j][j + k][1][0] * table[j][j + k][1][1] * table[j + k + 1][i][1][1], 
                            min_value)
            k += 1
        table[j][i] = [min_value, table_size]
        
print(table[0][-1][0])
