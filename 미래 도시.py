n, m = map(int, input().split())
adj = [[1e9] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      adj[i][j] = 0

for _ in range(m):
  i, j = map(int, input().split())
  adj[i][j] = 1
  adj[j][i] = 1

x, k = map(int, input().split())

def solve():
  for k in range(1, n + 1):
    for i in range(1, n + 1):
      for j in range(1, n + 1):
        adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

solve()

dist = adj[1][k] + adj[k][x]

if dist >= 1e9:
  print(-1)

else:
  print(dist)