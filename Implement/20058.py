# 20058
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(2**n)]
orders = list(map(int, input().split()))

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

def check_point(size):
    check_list = []
    for i in range(0, 2**n, size):
        for j in range(0, 2**n, size):
            check_list.append([i, j, i + size, j + size])

    return check_list
    
def rotate(origin_list):
    n, m = len(origin_list), len(origin_list[0])
    
    reverse_list = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            reverse_list[j][n-i-1] = origin_list[i][j]
    return reverse_list

def melt():
    melt_point = []
    for i in range(2**n):
        for j in range(2**n):
            count = 0
            for k in range(4):
                new_r, new_c = i + ad_r[k], j + ad_c[k]
                if new_r < 0 or new_r >= 2**n or new_c < 0 or new_c >= 2**n:
                    count += 1
                
                elif info[new_r][new_c] == 0:
                    count += 1
                
            if count >= 2:
                melt_point.append([i, j])

    return melt_point

for order in orders:
    size = 2 ** order
    my_list = check_point(size)
    
    for sr, sc, er, ec in my_list:
        origin_list = [[0] * size for _ in range(size)]
        
        for i in range(size):
            for j in range(size):
                origin_list[i][j] = info[sr + i][sc + j]
        
        reverse_list = rotate(origin_list)

        for i in range(size):
            for j in range(size):
                info[sr + i][sc + j] = reverse_list[i][j]
        
    melt_point = melt()

    for row, col in melt_point:
        info[row][col] = max(0, info[row][col] - 1)

visited = [[0] * (2**n) for _ in range(2**n)]

answer = [0]
for i in range(2**n):
    for j in range(2**n):
        if info[i][j] == 0 or visited[i][j]:
            continue
        
        start = [[i, j]]
        visited[i][j] = 1
        result = 1

        while start:
            r, c = start.pop()
            
            for k in range(4):
                new_r, new_c = r + ad_r[k], c + ad_c[k]
                if new_r < 0 or new_r >= 2**n or new_c < 0 or new_c >= 2**n:
                    continue

                if info[new_r][new_c] == 0 or visited[new_r][new_c]:
                    continue
                
                start.append([new_r, new_c])
                visited[new_r][new_c] = 1
                result += 1
        answer.append(result)

answer.sort()
print(sum(map(sum, info)))
print(answer[-1])
