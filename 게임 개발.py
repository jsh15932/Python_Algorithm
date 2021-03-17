n, m = map(int, input().split())
x, y, dir = map(int, input().split())

for i in range(n):
  for j in range(m):
    d[i][j] = 0

d[x][y] = 1
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def left():
    global dir
    dir -= 1

    if dir == -1:
        dir = 3

cnt = 1
t = 0

while True:
    left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt+= 1
        t = 0
        continue

    else:
        t += 1

    if t == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        
        else:
            break

        t = 0

print(cnt)