#1495 기타리스트 - 볼륨 조절
import sys
m = sys.stdin.readline

count, start, end = map(int, m().split(' '))

# up, down 가능만 확인
answer = [[0] * (end + 1) for _ in range(count + 1)]
volume = list(map(int, m().split(' ')))

for i in range(count+1):
    if i == 0:
        answer[i][start] = 1
    
    else:
        for j in range(end + 1):
            # 이전 볼륨 설정 가능일때, + - 연산
            if answer[i-1][j] == 1:
                up, down = j + volume[i-1], j - volume[i-1]
                if up <= end:
                    answer[i][up] = 1
                
                if down >= 0:
                    answer[i][down] = 1

for i in range(end, -1, -1):
    if answer[-1][i] == 1:
        print(i)
        sys.exit()
    
print(-1)
