# 16434
import sys, copy
input = sys.stdin.readline

n, hit = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

# 용사 최대 HP 구하기 위한 사전 탐색
hp, test_hit = 0, copy.deepcopy(hit)
for t, a, h in room:
    if t == 1:
        hit_chance = h // test_hit + min(1, h % test_hit)
        hp += (a * (hit_chance - 1))

    if t == 2:
        test_hit += a
        hp += h

        
# 이분 탐색
left, right = 1, hp*2
result = 0

while left <= right:
    mid = (left + right) // 2
    current_hp = (left + right) // 2
    st = False
    hit_point = copy.deepcopy(hit)
    for t, a, h in room:
        if t == 1:
            hit_chance = h // hit_point + min(1 , h % hit_point)
            current_hp -= (a * (hit_chance - 1))
    
        if current_hp <= 0:
            st = True
            break

        if t == 2:
            hit_point += a
            current_hp = min(mid, current_hp + h)
    # print(st, mid, hit_point, current_hp)
    if st: # 중간에 hp 0 이하
        left = mid + 1
    
    else:
        result = mid
        right = mid - 1

print(result)
