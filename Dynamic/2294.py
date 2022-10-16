import sys
m = sys.stdin.readline

num, target = map(int, m().split())
coin = [int(m()) for _ in range(num)]
answer = [10001] * (target+1)

coin.sort()
answer[0] = 0
for i in range(num):
    for j in range(coin[i], target+1):
        answer[j] = min(answer[j-coin[i]] + 1, answer[j])

if answer[target] == 10001:
    print(-1)
else:
    print(answer[target])
