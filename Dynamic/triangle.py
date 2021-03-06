#프로그래머스 정수삼각형

def solution(triangle):
    answer = []
    for k in range(1, len(triangle) + 1):
        answer.append([0] * k)
    
    for i in range(len(answer)):
        for j in range(len(triangle[i])):
            print(i, j)
            if i == 0:
                answer[i][j] = triangle[i][j]
            
            elif j == 0 :
                answer[i][j] = triangle[i-1][j] + triangle[i][j]
            
            elif j == len(triangle[i]) -1:
                answer[i][j] = triangle[i-1][j-1] + triangle[i][j]
                
            else:
                answer[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
            
    return max(answer[-1])
