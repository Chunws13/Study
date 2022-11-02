# 2206
import sys, heapq
m = sys.stdin.readline

row, col = map(int, m().split())
answer = [[[0] * 2 for _ in range(col)] for _ in range(row)]

info = []
for _ in range(row):
    info.append(list(map(int, m().strip())))

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

start = [[1, 0, 0, 1]]

while start:
    t, r, c, chance = heapq.heappop(start)
    if r == row-1 and c == col-1:
        print(t)
        sys.exit()
    
    for i in range(4):
        new_r, new_c = r + ad_r[i], c + ad_c[i]
        if 0 <= new_r < row and 0 <= new_c < col and answer[new_r][new_c][chance] == 0:
            if info[new_r][new_c] == 0:
                answer[new_r][new_c][chance] = 1
                heapq.heappush(start, [t+1, new_r, new_c, chance])
            
            if info[new_r][new_c] == 1 and chance:
                answer[new_r][new_c][chance-1] = 1
                heapq.heappush(start, [t+1, new_r, new_c, chance-1])
    
print(-1)
