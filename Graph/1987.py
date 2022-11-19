import sys
input = sys.stdin.readline

r, c = map(int, input().split())
info = [list(map(str, input().strip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

result = 1

def checker(row, col, answer, visited_word):
    global info, result
    result = max(answer, result)
    
    for i in range(4):
        new_r, new_c = ad_r[i] + row , ad_c[i] + col
        if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
            continue
        
        if info[new_r][new_c] not in visited_word:
            checker(new_r, new_c, answer + 1, visited_word + info[new_r][new_c])
            
checker(0, 0, 1, info[0][0])  
print(result)
