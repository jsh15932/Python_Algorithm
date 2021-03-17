n, k = map(int, input().split())
cnt = 0

while True:
  if n < k:
    break
  
  cnt += (n % k)
  n = n - (n % k)

  cnt += 1
  n //= k

cnt += (n - 1)

print(cnt)