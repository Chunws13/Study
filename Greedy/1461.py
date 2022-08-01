import sys
m = sys.stdin.readline

b_num, limit = map(int, m().split())
o_info = list(map(int, m().split()))

left, right = [0], [0]

for o in o_info:
    if o > 0:
        right.append(o)
    else:
        left.append(o)

right.sort(reverse=True)
left.sort()

answer = 0
if right[0] > abs(left[0]):
    answer += right[0]
    right = right[limit:]

elif right[0] < abs(left[0]):
    answer += abs(left[0])
    left = left[limit:]

else:
    if len(right) > len(left):
        answer += right[0]
        right = right[limit:]
    else:
        answer += abs(left[0])
        left = left[limit]

while right:
    answer += right[0] * 2    
    right = right[limit:]

while left:
    answer += abs(left[0]) * 2
    left = left[limit:]

print(answer)
