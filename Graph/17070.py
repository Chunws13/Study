# 1103
import sys
# sys.setrecursionlimit(10**6) <- 포함된 상태로 Pypy 제출 시 메모리 초과
input = sys.stdin.readline

size = int(input())
info = [list(map(int, input().split())) for _ in range(size)]
result = 0

def solve(row, col, logic):
    global result
    if row == size-1 and col == size-1:
        result += 1
        return
    if row == size-1 and logic == 'v':
        return
    
    if col == size-1 and logic == 'w':
        return
    
    if logic == 'w' or logic == 'd': # 가로
        if col + 1 < size and info[row][col + 1] == 0:
            solve(row, col + 1, 'w')
    
    if logic == 'v' or logic == 'd': # 세로
        if row + 1 < size and info[row + 1][col] == 0:
            solve(row + 1, col, 'v')
    
    if row + 1 < size and col + 1 < size:
        if info[row][col+1] == 0 and info[row+1][col] == 0 and info[row+1][col+1] == 0:
            solve(row+1, col+1, 'd')

if info[-1][-1] == 1:
    print(0)

else:
    solve(0, 1, 'w')
    print(result)
