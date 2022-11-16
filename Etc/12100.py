import sys, copy
m = sys.stdin.readline

size = int(m())
origin = [list(map(int, m().split())) for _ in range(size)]

def up(origin, size):
    info = copy.deepcopy(origin)
    for i in range(size):
        tmp = []
        for j in range(size):
            if info[j][i] != 0:
                tmp.append(info[j][i])
            info[j][i] = 0
        
        result_tmp = []
        for t in range(len(tmp)):
            if tmp[t] == 0:
                continue
            
            if t != len(tmp)-1 and tmp[t] == tmp[t+1]:
                tmp[t], tmp[t+1] = tmp[t] * 2, 0
            
            result_tmp.append(tmp[t])
            
        for j, k in enumerate(result_tmp):
            info[j][i] = k
        
    return info

def down(origin, size):
    info = copy.deepcopy(origin)
    for i in range(size):
        tmp = []
        for j in range(size-1, -1, -1):
            if info[j][i] != 0:
                tmp.append(info[j][i])
            info[j][i] = 0
        
        result_tmp = []
        for t in range(len(tmp)):
            if tmp[t] == 0:
                continue
            
            if t != len(tmp)-1 and tmp[t] == tmp[t+1]:
                tmp[t], tmp[t+1] = tmp[t] * 2, 0
            
            result_tmp.append(tmp[t])
            
        for j, k in enumerate(result_tmp):
            info[-(j+1)][i] = k
    
    return info

def left(origin, size):
    info = copy.deepcopy(origin)
    for i in range(size):
        tmp = []
        for j in range(size):
            if info[i][j] != 0:
                tmp.append(info[i][j])
            info[i][j] = 0
        
        result_tmp = []
        for t in range(len(tmp)):
            if tmp[t] == 0:
                continue
            
            if t != len(tmp)-1 and tmp[t] == tmp[t+1]:
                tmp[t], tmp[t+1] = tmp[t] * 2, 0
            
            result_tmp.append(tmp[t])

        for j, k in enumerate(result_tmp):
            info[i][j] = k
    
    return info

def right(origin, size):
    info = copy.deepcopy(origin)
    for i in range(size):
        tmp = []
        for j in range(size-1, -1, -1):
            if info[i][j] != 0:
                tmp.append(info[i][j])
            info[i][j] = 0
        
        result_tmp = []
        for t in range(len(tmp)):
            if tmp[t] == 0:
                continue
            
            if t != len(tmp)-1 and tmp[t] == tmp[t+1]:
                tmp[t], tmp[t+1] = tmp[t] * 2, 0
            
            result_tmp.append(tmp[t])
        
        for j, k in enumerate(result_tmp):
            info[i][-(j+1)] = k
    
    return info

def max_check(origin):
    return max(map(max, origin))

def calculate(origin, size):
    return [left(origin, size), right(origin, size), up(origin, size), down(origin, size)]

all_list, answer = [origin], 0
for _ in range(5):
    tmp_list, all_list = all_list, []
    for r in tmp_list:
        for tmp in calculate(r, size):
            all_list.append(tmp)

for a in all_list:
    answer = max(answer, max_check(a))
print(answer)
