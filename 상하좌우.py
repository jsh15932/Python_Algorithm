n = int(input())
x = 1
y = 1
order = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dir = ['L', 'R', 'U', 'D']

for i in order:
  for j in range(len(dir)):
    if i == dir[j]:
      nx = x + dx[j]
      ny = y + dy[j]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  x = nx
  y = ny

print(x, y)