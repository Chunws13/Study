# 행렬
import sys
m = sys.stdin.readline

row, col = map(int, m().split())

a, b, answer = [], [], 0

for r in range(row):
    a.append(list(map(int, m().strip())))

for r in range(row):
    b.append(list(map(int, m().strip())))

# 특정 위치 뒤집기
def reverse(target, row, col):
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            target[r][c] = (target[r][c] + 1) % 2

# 뒤집는 부분 탐색
for r in range(row - 2):
    for c in range(col - 2):
        if a[r][c] != b[r][c]:
            reverse(a, r, c)
            answer += 1

# 일치 검사
for r in range(row):
    if a[r] != b[r]:
        answer = -1
        break

print(answer)