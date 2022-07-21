# 주사위 면의 합이 최소값이 될 수 있도록
import sys
m = sys.stdin.readline

dice = int(m())
dice_info = list(map(int, m().split()))

two_side = 100
# 2개면 최소값
for i in range(6):
    for k in range(6):
        if i == k or i + k ==5 :
            continue
        two_side = min(two_side, dice_info[i] + dice_info[k])

three_side = 150
for i in range(6):
    for k in range(6):
        if i == k or i + k == 5:
            continue
        for l in range(6):
            if i == l or k == l or i + l == 5 or k + l == 5:
                continue
            
            three_side = min(three_side, dice_info[i] + dice_info[k] + dice_info[l])
                

# 주사위 1개일 때 - 최대값을 제외한 전체
if dice == 1:
    print(sum(dice_info) - max(dice_info))

else:
    min_dice = min(dice_info)
    
    # 3개면 노출 - 모서리 4개
    imp_three = 4 * three_side

    # 2개면 노출 - 상단 (n - 2) * 4 개 + 4면 모서리 
    imp_two = (dice * 2 -3) * 4 * two_side
    side = (dice - 2) * (dice -1) * min_dice * 4
    top = (dice - 2) * (dice - 2) * min_dice
    print(imp_two + imp_three + side + top)
