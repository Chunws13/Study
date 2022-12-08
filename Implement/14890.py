# 14890
import sys
input = sys.stdin.readline

size, length = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(size)]
answer = 0

# 가로, 1차 검사
def check(i):
    tmp_road = [0] * size
    for j in range(size-1):
        
        # 도로 높이차 2이상
        if abs(road[i][j] - road[i][j+1]) > 1:
            return 0
        
        # 내리막 
        if road[i][j] - road[i][j+1] == 1:
            
            if max(road[i][j+1: j+length+1]) != min(road[i][j+1: j+length+1]):
                return 0
                
            elif len(road[i][j+1: j+length+1]) < length:
                return 0
            
            for k in range(j+1, j+length+1):
                tmp_road[k] = 1
        
        # 오르막
        if road[i][j] - road[i][j+1] == -1:
            
            if j-length+1 < 0:
                return 0
            
            elif max(road[i][j-length+1: j+1]) != min(road[i][j-length+1: j+1]):
                return 0
            
            elif sum(tmp_road[j-length+1:j+1]) != 0:
                return 0

    return 1

for i in range(size):
    answer += check(i)
    
road = list(map(list, zip(*road)))

for i in range(size):
    answer += check(i)

print(answer)
