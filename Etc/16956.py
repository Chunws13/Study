import sys
m = sys.stdin.readline

r, c = map(int, m().split())
info = []
for _ in range(r):
    info.append(list(map(str, m().strip())))

visited = [[0] * c for _ in range(r)]
sheep, wolf = [], []

for i in range(r):
    for j in range(c):
        if info[i][j] == 'S':
            sheep.append([i,j])
        
        if info[i][j] == 'W':
            wolf.append([i, j])

ad_r, ad_c = [1, -1, 0, 0], [0, 0, 1, -1]

while sheep:
  sr, sc = sheep.pop()
  for k in range(4):
      new_r, new_c = sr + ad_r[k], sc + ad_c[k]
      if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
          continue

      if info[new_r][new_c] == '.':
        info[new_r][new_c] = 'D'

while wolf:
  wr, wc = wolf.pop()
  
  for k in range(4):
      new_r, new_c = wr + ad_r[k], wc + ad_c[k]
      
      if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
          continue
      
      if visited[new_r][new_c] == 1 or info[new_r][new_c] == 'D':
          continue
      
      if info[new_r][new_c] == 'S':
          print(0)
          sys.exit()
      
      else:
        wolf.append([new_r, new_c])
        visited[new_r][new_c] = 1

print(1)
for i in info:
  print(''.join(i))
