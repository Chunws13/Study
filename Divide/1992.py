# 쿼드트리 - 분할정복
import sys
m = sys.stdin.readline

size = int(m())
video = [list(map(int, m().strip())) for _ in range(size)]

def solution(video, size):
    if size == 1:
        return str(video[0][0])
    
    elif max(map(max, video)) == min(map(min, video)):
        return str(max(map(max, video)))
    
    else:
        slice = size//2
        quarter_1, quarter_2, quarter_3, quarter_4 = [], [], [], []
        
        for i in range(slice):
            quarter_1.append(video[i][:slice])
            quarter_2.append(video[i][slice:])
        
        for j in range(slice, size):
            quarter_3.append(video[j][:slice])
            quarter_4.append(video[j][slice:])
        
        return "(" + solution(quarter_1, slice) + solution(quarter_2, slice) + solution(quarter_3, slice) + solution(quarter_4, slice) + ")"

print(solution(video, size))
