n = int(input())
cnt = [0] * 10001
res = -1
max_value = 0

for i in range(n):
  data = int(input())
  cnt[data] += 1

  if max_value < cnt[data]:
    max_value = cnt[data]
    res = data

print(res)