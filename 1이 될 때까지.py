n, k = map(int, input().split())
cnt = 0

while True:
  cnt += (n % k)
  n = n - (n % k)
  
  if n < k:
    break

  cnt += 1
  n //= k

cnt += (n - 1)

print(cnt)