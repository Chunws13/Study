import sys
m = sys.stdin.readline

case = int(m())

def get_top(name):
    if friend[name] == name:
        return name
    
    else:
        n = get_top(friend[name])
        friend[name] = n
        return friend[n]

def union(f1, f2):
    new_f1, new_f2 = get_top(f1), get_top(f2)
    if new_f1 != new_f2:
        friend[new_f2] = new_f1
        f_size[new_f1] += f_size[new_f2]

answer = []
for _ in range(case):
    f_num = int(m())
    f_info = [list(map(str, m().split())) for _ in range(f_num)]
    friend, f_size = {}, {}
    
    for f1, f2 in f_info:
        if f1 not in friend:
            friend[f1] = f1
            f_size[f1] = 1
        
        if f2 not in friend:
            friend[f2] = f2
            f_size[f2] = 1
            
        union(f1, f2)
        
        print(f_size[get_top(f1)])
