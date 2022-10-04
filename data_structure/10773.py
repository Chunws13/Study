# 10773
import sys
m = sys.stdin.readline

num = int(m())
my_list = []
for _ in range(num):
    write_num = int(m())
    if write_num != 0:
        my_list.append(write_num)
    else:
        my_list.pop()
        
print(sum(my_list))
