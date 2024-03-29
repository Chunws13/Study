# Study

# Dictionary 트리
    point = floor['start']
    for i in range(1, len(info)):
        point[info[i]] = point.get(info[i], {})
        point = point[info[i]]


# 2차원 리스트 행/열 반전
기존 리스트 = Origin_list / 반전 리스트 = Reverse_list

    Reverse_list = list(map(list, zip(*Origin_list)))

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
    
# 2차원 배열 외벽 순환 / ex. BOJ - 17144

    for i in range(2):
        sr, sc = air_cleaner[i]
        if i == 0: 반시계 방향 순환
            if sc == 0:
                sr, sc, idx = sr - 1, sc, 0

            else:
                sr, sc, idx = sr, sc - 1, 3
            
            mr, mc = [-1, 0, 1, 0], [0, 1, 0, -1]
        
            while [sr, sc] != air_cleaner[i]:
                if sr + mr[idx] == air_cleaner[i][0] and sc + mc[idx] == air_cleaner[i][1]:
                    break
                    
                elif 0 <= sr + mr[idx] <= air_cleaner[i][0] and 0 <= sc + mc[idx] < c:
                    condition[sr][sc] = condition[sr + mr[idx]][sc + mc[idx]]
                    condition[sr + mr[idx]][sc + mc[idx]] = 0
                    sr, sc = sr + mr[idx], sc + mc[idx]

                else:
                    idx = (idx + 1) % 4
        else:
            if sc == 0: 시계 방향 
                sr, sc, idx = sr + 1, sc, 0

            else:
                sr, sc, idx = sr, sc - 1, 3

            mr, mc = [1, 0, -1, 0], [0, 1, 0, -1]

            while [sr, sc] != air_cleaner[i]:
                if sr + mr[idx] == air_cleaner[i][0] and sc + mc[idx] == air_cleaner[i][1]:
                    break
                
                elif air_cleaner[i][0] <= sr + mr[idx] < r and 0 <= sc + mc[idx] < c:
                    condition[sr][sc] = condition[sr + mr[idx]][sc + mc[idx]]
                    condition[sr + mr[idx]][sc + mc[idx]] = 0
                    sr, sc = sr + mr[idx], sc + mc[idx]

                else:
                    idx = (idx + 1) % 4

# 세그먼트 트리 - 구간 합 기준
    ## 생성
    def init(start, end, idx):
        if start == end:
            table[idx] = info[start]
            return table[idx]

        mid = (start + end) // 2
        table[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx*2 + 1)
        return table[idx]
    
    ## 구간합
    def calc(start, end, idx, left, right):
        if left <= start and end <= right:
            return table[idx]

        if end < left or start > right:
            return 0

        mid = (start + end) // 2
        return calc(start, mid, idx*2, left, right) + calc(mid + 1, end, idx*2 + 1, left, right)
    
    ## 업데이트
    def update(start, end, idx, point, value):
        if point < start or point > end:
            return

        if start == end:
            table[idx] = value
            return

        mid = (start + end) // 2
        update(start, mid, idx * 2, point, value)
        update(mid + 1, end, idx * 2 + 1, point, value)
        table[idx] = table[idx*2] + table[idx *2 + 1]
