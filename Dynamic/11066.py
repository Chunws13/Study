import sys
m = sys.stdin.readline

case = int(m())
for _ in range(case):
    num = int(m())
    info = list(map(int, m().split()))
    sum_info = [info[0]]
    answer = [[0] * num for _ in range(num)]

    for i in range(1, num):
        sum_info.append(sum_info[-1] + info[i])

    for i in range(num-1):
        answer[i][i+1] = info[i] + info[i+1]

    for j in range(2, num):
        i = 0

        while i + j < num:
            for k in range(i, i+j):
                tmp = sum_info[i + j] - sum_info[i - 1] if i != 0 else sum_info[i + j]

                if answer[i][i + j] == 0:
                    answer[i][i + j] = answer[i][k] + answer[k + 1][i + j] + tmp

                else:
                    answer[i][i + j] = min(answer[i][k] + answer[k + 1][i + j] + tmp, answer[i][i+j])
            i += 1

    print(answer[0][-1])
