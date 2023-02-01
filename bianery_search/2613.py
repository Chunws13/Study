import sys, math, copy
input = sys.stdin.readline

n, m = map(int, input().split())
info = list(map(int, input().split()))

max_value, m_list = math.inf, []
left, right = max(info), sum(info)

while left <= right:
    mid = (left + right) // 2
    t_value, t_info = 0, []
    now, marble = 0, 0
    cnt = 0
    for i in range(n):
        if now + info[i] > mid:
            t_info.append(marble)
            now = 0
            marble = 0
            cnt += 1
        
        elif m - cnt > n - i: # 최대값 한계까지 나누지 않고 분리할 때
            if marble > 1:
                t_info.append(marble)
            
            else:
                t_info.append(1)

            now = 0
            marble = 0
        
        now += info[i]
        marble += 1
    
    if marble:
        t_info.append(marble)
        cnt += 1

    if cnt > m:
        left = mid + 1

    else:
        max_value = mid
        m_list = copy.deepcopy(t_info)
        right = mid - 1

print(max_value)
print(*m_list)
