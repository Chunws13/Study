import sys
input = sys.stdin.readline

sensor_num = int(input())
center = int(input())

info = sorted(list(map(int, input().split())), reverse=True)
distance = [info[i] - info[i+1] for i in range(sensor_num-1)]

if sensor_num <= center:
    print(0)
    sys.exit()

distance.sort()
for _ in range(center-1):
    distance.pop()
    

print(sum(distance))
