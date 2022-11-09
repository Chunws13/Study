import sys
m = sys.stdin.readline

size = int(m())
info = []
for _ in range(size):
    info.append(list(map(int, m().split())))

visited = [[0] * size for _ in range(size)]

ad_r, ad_c = [1, -1, 0, 0, 0], [0, 0, 1, -1, 0]

def check(r, c):
    for k in range(5):
        new_r, new_c = r + ad_r[k], c + ad_c[k]
        if visited[new_r][new_c] == 1:
            return False

    return True

def mark(r, c):
    global total
    for k in range(5):
        total += info[r + ad_r[k]][c + ad_c[k]]
        visited[r + ad_r[k]][c + ad_c[k]] = 1

def remark(r, c):
    global total
    for k in range(5):
        total -= info[r + ad_r[k]][c + ad_c[k]]
        visited[r + ad_r[k]][c + ad_c[k]] = 0

def solution(cnt):
    global answer, total
    if cnt == 3:
        answer = min(answer, total)
        return answer

    for i in range(1, size-1):
        for j in range(1, size-1):
            if check(i, j):
                
                mark(i, j)
                solution(cnt+1)
                remark(i, j)

answer, total = 1000001, 0
solution(0)
print(answer)
