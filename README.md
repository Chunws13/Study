# Study


# 2차원 배열 회전
def rotate(o_list, index):
    n = len(o_list) - 행 길이
    m = len(o_list[0]) - 열 길이 계산
    
    # 270도 회전
    if index == 1:
        new = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new[m-j-1][i] = o_list[i][j]
        return new
    
    # 180도 회전
    elif index == 2:
        new = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new[n-i-1][m-j-1] = o_list[i][j]
        return new
    
    
    # 90도 회전
    elif index == 3: 
        new = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new[j][n-i-1] = o_list[i][j]
        return new
    
    else:
        return o_list


# 2차원 리스트 행/열 반전
기존 리스트 = Origin_list / 반전 리스트 = Reverse_list

Reverse_list = list(map(list, zip(*Origin_list)))
