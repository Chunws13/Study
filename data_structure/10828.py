# 10828
import sys
m = sys.stdin.readline

order_num = int(m())
my_list = []
# push / pop / size / empty / top
def action(order, num=None):
    if order == 'push':
        my_list.append(num)
        return 
    
    if order == 'pop':
        if my_list:
            m = my_list.pop()
            return m
        return -1
    
    if order == 'size':
        return len(my_list)    

    if order == 'empty':
        if my_list:
            return 0
        return 1    
    
    if order == 'top':
        if my_list:
            return my_list[-1]
        return -1
    
order = [list(map(str, m().split())) for _ in range(order_num)]

for o in order:
    if o[0] == 'push':
        action(o[0], o[1])
    else:
        print(action(o[0]))
