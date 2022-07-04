# 프로그래머스 - 등굣길

def solution(m, n, puddles):
    road = []
    for i in range(n):
        road.append([0] * m)
    
    for p in puddles:
        b, a = p[0]-1, p[1]-1
        road[a][b] = -1
    
    # 시작 지점 1 할당
    road[0][0] = 1
        
    for r1 in range(len(road)):
        for r2 in range(len(road[r1])):
            # 시작점 or 웅덩이 지점 계산 x
            if r1 == 0 and r2 == 0 or road[r1][r2] == -1:
                pass
            
            # 길 최상단: 좌측 웅덩이 없는 경우에만 좌측 길 할당
            elif r1 == 0 and road[r1][r2-1] != -1:
                road[r1][r2] = road[r1][r2-1]
            
            # 길 좌측: 위쪽 웅덩이 없는 경우에만 위쪽 길 할당
            elif r2 == 0 and road[r1-1][r2] != -1:
                road[r1][r2] = road[r1-1][r2]
            
            # 좌측에 웅덩이 있는 경우
            elif road[r1-1][r2] == -1:
                road[r1][r2] = road[r1][r2-1]
            
            # 위쪽에 웅덩이 있는 경우
            elif road[r1][r2-1] == -1:
                road[r1][r2] = road[r1-1][r2]
            
            # 나머지 경우
            else:
                road[r1][r2] = (road[r1][r2-1] + road[r1-1][r2]) % 1000000007
                
    return road[-1][-1] % 1000000007
