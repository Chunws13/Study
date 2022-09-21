import sys
from collections import deque
m = sys.stdin.readline

tower = int(m())
t_info = list(map(int, m().split()))

t_wait, answer = deque([]), [0] * tower
idx = tower - 1
while t_info:
    t = t_info.pop()
    
    #인덱스 번호라 같이 저장
    t_wait.appendleft([idx, t])
    
    # 두 리스트 모두 요소 있음, 앞 리스트 마지막 보다 작을 때 마다 popleft
    while t_wait and t_info and t_info[-1] >= t_wait[0][1]:
        tw = t_wait.popleft()
        answer[tw[0]] = len(t_info)
    
    idx -= 1
    
    # popleft 되지 못하 요소들은 0 처리이므로 별도 조치 필요 없음

print(" ".join(map(str, answer)))
