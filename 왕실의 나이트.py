n = input()
r = int(n[1]) - 0
c = int(ord(n[0])) - int(ord('a')) + 1

dir = [
    (-2,-1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)
]

res = 0

for i in dir:
  nr = r + i[0]
  nc = c + i[1]

  if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
    res += 1

print(res)