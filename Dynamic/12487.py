# 12487
import sys
m = sys.stdin.readline

limit = int(m())
answer = [[0] * 8 for _ in range(limit+1)]
answer[0][0] = 1

for i in range(1, limit+1):
    answer[i][0] = (answer[i-1][1] + answer[i-1][2]) % 1000000007
    answer[i][1] = (answer[i-1][0] + answer[i-1][2] + answer[i-1][3]) % 1000000007
    answer[i][2] = (answer[i-1][0] + answer[i-1][1] + answer[i-1][3] + answer[i-1][5]) % 1000000007
    answer[i][3] = (answer[i-1][1] + answer[i-1][2] + answer[i-1][4] + answer[i-1][5]) % 1000000007
    answer[i][4] = (answer[i-1][3] + answer[i-1][5] + answer[i-1][6]) % 1000000007
    answer[i][5] = (answer[i-1][4] + answer[i-1][3] + answer[i-1][2] + answer[i-1][7]) % 1000000007
    answer[i][6] = (answer[i-1][4] + answer[i-1][7]) % 1000000007
    answer[i][7] = (answer[i-1][6] + answer[i-1][5]) % 1000000007

print(answer[limit][0] % 1000000007)
