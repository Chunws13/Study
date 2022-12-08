# 17140
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(3)]

answer = 0
def solve_r():
    result_list = []
    
    for i in info:
        empty_dic, empty_list = {}, []
        for j in i:
            
            if j == 0:
                continue
            
            empty_dic[j] = empty_dic.get(j, 0) + 1
        _dic = sorted(empty_dic.items(), key=lambda x:(x[1], x[0]))
        
        for a, b in _dic:
            empty_list += [a, b]
        
        result_list.append(empty_list)
    
    max_len = max(map(len, result_list))
    
    for i in range(len(result_list)):
        result_list[i] = result_list[i] + [0] * (max_len - len(result_list[i]))
        result_list[i] = result_list[i][:100]
    
    return result_list
    
while True:
    try:
        if info[r-1][c-1] == k:
            print(answer)
            break
        answer += 1
        
    except:
        answer += 1
        
    if answer > 100:
        print(-1)
        break
    
    if len(info) >= len(info[0]):
        info = solve_r()
        
    else:
        info = list(map(list, zip(*info)))
        info = solve_r()
        info = list(map(list, zip(*info)))
