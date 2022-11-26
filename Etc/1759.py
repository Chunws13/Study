import sys
input = sys.stdin.readline

pw_len, case = map(int, input().split())
candidate = list(map(str, input().split()))

candidate.sort()
answer = []

def check(word):
    count, ncount = 0, 0
    for c in word:
        if c in ['a', 'e', 'i', 'o', 'u']:
            count += 1
        else:
            ncount += 1
        
    if count >= 1 and ncount >= 2:
        return True
        
    return False

def pw_make(word, num):
    global answer, candidate
    if len(word) == pw_len:
        if check(word):
            answer.append(word)
        
        else:
            return
    
    for i in range(num, case):
        add_word = candidate[i]
        pw_make(word + add_word, i+1)
    
pw_make('', 0)
answer.sort()

print("\n".join(answer))
