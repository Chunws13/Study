# 영어 단어 숫자 합, 1339번 변형
import sys

m = sys.stdin.readline

# 입력 정보
w_num = int(m())
w_list = [list(map(str, m().strip())) for _ in range(w_num)]
w_info = {}

# 자리수 체크 + 시작수 여부 확인 (시작 수 1로 표기)
for i in range(w_num):
    for j in range(len(w_list[i])):
        if w_list[i][j] not in w_info:
            w_info[w_list[i][j]] = [10 ** (len(w_list[i]) -j -1), 0]
        
        elif w_list[i][j] in w_info:
            w_info[w_list[i][j]][0] += 10 ** (len(w_list[i]) -j -1)
        
        if j == 0:
            w_info[w_list[i][j]][1] = 1

new_info = sorted(w_info.items(), key=lambda x: (x[1][0], -x[1][1]))

start = 10 - len(new_info)
index = {}
for s in range(start, 10):
    index[s] = True

answer = 0
for n in new_info:
    for i in index:
        # 시작 수는 0이 될 수 
        if n[1][1] == 1 and i == 0:
            continue
        
        if index[i]:
            answer += n[1][0] * i
            index[i] = False
            break

print(answer)
