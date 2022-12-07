# 21608
import sys
input = sys.stdin.readline

size = int(input())
info = [[] for _ in range(size**2 + 1)]
room = [[0] * size for _ in range(size)]
sequence = []

for _ in range(size**2):
    i = list(map(int, input().split()))
    sequence.append(i[0])
    info[i[0]] += i[1:]
    
ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]
score = [0, 1, 10, 100, 1000]
answer = 0

# 자리탐색 / 1. 인접 / 2. 빈칸 / 3. row 우선 / 4. col 우선

def find(people, friends):
    favor, empty, row, col = -1, -1, 0, 0
    for r in range(size):
        for c in range(size):
            f, e = 0, 0            
            
            if room[r][c]:
                continue
            
            for i in range(4):
                new_r, new_c = r + ad_r[i], c + ad_c[i]
                if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:
                    continue
                
                
                if room[new_r][new_c] == 0:
                    e += 1
                
                if room[new_r][new_c] in friends:
                    f += 1
                
            if favor < f:
                favor, empty, row, col = f, e, r, c
            
            elif favor == f and empty < e:
                favor, empty, row, col = f, e, r, c

    room[row][col] = people

def check(row, col, people):
    result = 0
    friend_list = info[people]
    
    for i in range(4):
        new_r, new_c = row + ad_r[i], col + ad_c[i]
        if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:
            continue
        
        if room[new_r][new_c] in friend_list:
            result += 1
    
    return score[result]
    
for s in sequence:
    find(s, info[s])

for r in range(size):
    for c in range(size):
        answer += check(r, c, room[r][c])

print(answer)
