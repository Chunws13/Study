# 16724
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
zone = [list(map(str, input().strip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

move = {'R': [0, 1], 'L': [0, -1], 'D' : [1, 0], 'U': [-1, 0]}
count = 1
for i in range(r):
    for j in range(c):
        if visited[i][j]:
            continue
        
        start = [[i, j]]
        visited[i][j] = count
        while start:
            row, col = start.pop()
            for k in 'RLDU':
                new_move = move[k]
                new_r, new_c = row + new_move[0], col + new_move[1]
                if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c or visited[new_r][new_c]:
                    continue
                
                # 되돌아오는 방향
                next_zone = move[zone[new_r][new_c]]
                if new_r + next_zone[0] == row and new_c + next_zone[1] == col:
                    visited[new_r][new_c] = count
                    start.append([new_r, new_c])
                
                # 나아가는 방향
                p_zone = move[zone[row][col]]
                if new_r == row + p_zone[0] and new_c == col + p_zone[1]:
                    visited[new_r][new_c] = count
                    start.append([new_r, new_c])
                
        count += 1

print(max(map(max, visited)))
