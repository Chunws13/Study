# 뒤집기 2
import sys
m = sys.stdin.readline

row, col = map(int, m().split())

coin = []
answer = 0

for _ in range(row):
    coin.append(list(map(int, m().strip())))

def reverse(coin, row, col):
    for r2 in range(row +1):
        for c2 in range(col +1):
            coin[r2][c2] = (coin[r2][c2] + 1) % 2
            
for r in range(row-1, -1, -1):
    for c in range(col-1, -1, -1):
        if coin[r][c] == 1:
            answer += 1
            reverse(coin, r, c)

print(answer)