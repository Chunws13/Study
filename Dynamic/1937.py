#1937
import sys
sys.setrecursionlimit(10**6)
m = sys.stdin.readline

size = int(m())

info = []
for _ in range(size):
    info.append(list(map(int, m().split())))

answer = [[0] * size for _ in range(size)]
ad_x, ad_y = [1, -1, 0, 0], [0, 0, 1, -1]

def solution(r, c):
    if answer[r][c] == 0:
        
        for k in range(4):
                new_r, new_c = r + ad_y[k], c + ad_x[k]
                if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:
                    continue
                
                # 이웃 숫자 보다 작다면
                # 이웃 숫자가 갈 수 있는 거리에서 + 1만 큼 더 갈 수 있음
                if info[r][c] < info[new_r][new_c]:
                    answer[r][c] = max(answer[r][c], solution(new_r, new_c)+1)
        
    return answer[r][c]

result = 1
for i in range(size):
    for j in range(size):
        result = max(solution(i, j), result)
    
print(result)
