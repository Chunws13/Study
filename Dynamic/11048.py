# 11048
import sys
m = sys.stdin.readline

tr, tc = map(int, m().split())
info = []
answer = [[0] * tc for _ in range(tr)]

for i in range(tr):
    info.append(list(map(int, m().split())))

ad_r, ad_c = [-1, 0], [0, -1]
answer[0][0] = info[0][0]

for r in range(tr):
    for c in range(tc):
        for i in range(2):
            new_r, new_c = r + ad_r[i], c + ad_c[i]
            if new_r < 0 or new_r >= tr or new_c < 0 or new_c >= tc:
                continue
            answer[r][c] = max(info[r][c] + answer[new_r][new_c], answer[r][c])

print(answer[tr-1][tc-1])
