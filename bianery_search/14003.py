import sys
input = sys.stdin.readline

size = int(input())
info = list(map(int, input().split()))

table = [0] * size # 인덱스 저장 배열
answer = []
for i in range(size):
    number = info[i]
    if len(answer) == 0 or answer[-1] < number:
        answer.append(number)
        table[i] = len(answer)-1 # 인덱스 좌표 수정 없이 입력
    
    else:
        left, right = 0, len(answer) -1
        while left <= right:
            mid = (left + right) // 2
            if answer[mid] == number:
                left = mid
                break

            if answer[mid] < number:
                left = mid + 1

            else:
                right = mid -1

        answer[left] = number
        table[i] = left # info[i] 값, answer[-1] 보다 작으므로 인덱스 위치 조정

step_1 = len(answer)
print(step_1)
result = []

# 인덱스 탐색 - 역순
for i in range(size-1, -1, -1):
    if table[i] == step_1-1:
        result.append(info[i])
        step_1 -= 1

print(*result[::-1])
