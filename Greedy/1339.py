# 영어 단어 수학
import sys

m = sys.stdin.readline

# 입력 정보
w_num = int(m())
w_list = [list(map(str, m().strip())) for _ in range(w_num)]
w_info = {}

# 자리수, 
for i in range(w_num):
    for j in range(len(w_list[i])):
        if w_list[i][j] not in w_info:
            w_info[w_list[i][j]] = 10 ** (len(w_list[i]) -j -1)
        
        else:
            w_info[w_list[i][j]] += 10 ** (len(w_list[i]) -j -1)

new_info = sorted(w_info.items(), key=lambda x: x[1], reverse = True)

index = 9
answer = 0
for n in new_info:
    answer += n[1] * index
    index -=1

print(answer)
