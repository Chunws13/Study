import sys
input = sys.stdin.readline

target = int(input())
a, b = map(int, input().split())

pizza_a = [int(input()) for _ in range(a)]
pizza_b = [int(input()) for _ in range(b)]

# 순환 배열의 누적합
# 전체 합은 중복됨
sum_a, sum_b = {sum(pizza_a) : 1}, {sum(pizza_b) : 1}

def get_sum(sum_array, array):
    for i in range(len(array)):
        tmp = 0
        # 바로 다음 조각 이전 까지 누적합
        for j in range(i, i - len(array) + 1, -1):
            tmp += array[j]
            sum_array[tmp] = sum_array.get(tmp, 0) + 1

get_sum(sum_a, pizza_a)
get_sum(sum_b, pizza_b)

# 탐색 - dic 구조
result = 0
result += sum_a.get(target, 0) # 있으면 추가, 없으면 0 추가
result += sum_b.get(target, 0)

for piece_a in sum_a:
    piece_b = target - piece_a
    result += sum_b.get(piece_b, 0) * sum_a[piece_a]

print(result)
