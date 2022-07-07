# 스티커
import sys
m = sys.stdin.readline

case = int(m())
for _ in range(case):
    length = int(m())
    
    answer = [[0, 0] for _ in range(length +1)]
    sticker = [list(map(int, m().split(' '))) for _ in range(2)]
        
    for i in range(length + 1):
        if i == 0:
            continue
        
        if i == 1:
            answer[i][0] = sticker[0][i-1]
            answer[i][1] = sticker[1][i-1]
        
        elif i == 2:
            answer[i][0] = sticker[1][i-2] + sticker[0][i-1]
            answer[i][1] = sticker[0][i-2] + sticker[1][i-1]
        
        else:
            answer[i][0] = max(answer[i-1][1] + sticker[0][i-1], answer[i-2][1] + sticker[0][i-1])
            answer[i][1] = max(answer[i-1][0] + sticker[1][i-1], answer[i-2][0] + sticker[1][i-1])
            
    print(max(answer[-1]))
