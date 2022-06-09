# RGB 거리

import sys
m = sys.stdin.readline

house_number = int(m())

house = [[0, 0, 0]]
for h in range(house_number):
    add_house = list(map(int, m().split()))
    house.append(add_house)

answer = [[0, 0, 0]]
for i in range(len(house)):
    if i > 0:
        r = min(answer[i-1][1], answer[i-1][2]) + house[i][0]
        g = min(answer[i-1][0], answer[i-1][2]) + house[i][1]
        b = min(answer[i-1][0], answer[i-1][1]) + house[i][2]
        answer.append([r, g, b])

print(min(answer[house_number]))
