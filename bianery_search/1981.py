# 1981
import sys, math
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = math.inf

adr, adc = [0, 0, 1, -1], [1, -1, 0, 0]
def path_find(left, right):
    if board[0][0] < left or board[0][0] > right:
        return False

    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    start = deque([[0, 0]])

    while start:
        r, c = start.popleft()

        if r == n-1 and c == n-1:
            return True

        for i in range(4):
            new_r, new_c = r + adr[i], c + adc[i]
            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n or visited[new_r][new_c]:
                continue
            
            if left <= board[new_r][new_c] <= right:
                start.append([new_r, new_c])
                visited[new_r][new_c] = 1
            
    return False

left, right = 0, 0
while right <= max(map(max, board)):
    if path_find(left, right):
        result = min(right - left, result)
        left += 1

    else:
        right += 1

print(result)
