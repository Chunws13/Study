#14501

import sys
m = sys.stdin.readline

counsel = int(m())
c_info = [list(map(int, m().split())) for i in range(counsel)]
answer = [0] * counsel

for i in range(counsel):
    value = c_info[i][1] if c_info[i][0] + i <= counsel else 0
    
    for j in range(i):
        if c_info[j][0] + j <= i:
            answer[i] = max(answer[i], value + answer[j])
    
    answer[i] = value if answer[i] == 0 else answer[i]

print(max(answer))
