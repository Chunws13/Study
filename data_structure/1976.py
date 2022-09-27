import sys
m = sys.stdin.readline

city = int(m())
info_num = int(m())
info = [[0] * (city+1)] + [[0] + list(map(int, m().split())) for _ in range(city)]

destination = [k for k in range(city+1)]
checker = list(map(int, m().split()))

def find(k):
  while k != destination[k]:
    k = destination[k]

  return k

def union(a, b):
  new_a = find(a)
  new_b = find(b)
  if new_a > new_b:
    destination[new_b] = new_a
  
  else:
    destination[new_a] = new_b
  

for i in range(1, city+1):
    for j in range(1, city+1):
        if info[i][j] == 1:
          union(destination[i], destination[j])
        
answer = []
while checker:
    c = checker.pop()
    while c != destination[c]:
        c = destination[c]
    
    answer.append(c)

if max(answer) == min(answer):
    print("YES")

else:
    print("NO")
