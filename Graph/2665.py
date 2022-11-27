import sys, heapq
input = sys.stdin.readline

size = int(input())
maze = [list(map(int, input().strip())) for _ in range(size)]
visited = [[-1] * size for _ in range(size)]

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

visited[0][0] = 1
start = [[0, 0, 0]]

while start:
    b, r, c = heapq.heappop(start)
    for i in range(4):
        new_r, new_c = ad_r[i] + r, ad_c[i] + c
        
        if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:
            continue
        
        if visited[new_r][new_c] != -1:
            continue
        
        if maze[new_r][new_c] == 1:
            visited[new_r][new_c] = b
            heapq.heappush(start, [b, new_r, new_c])
        
        else:
            visited[new_r][new_c] = b + 1
            heapq.heappush(start, [b + 1,  new_r, new_c])

print(visited[-1][-1])
