n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

ans1 = data[n - 1]
ans2 = data[n - 2]

cnt = int(m / (k + 1)) * k
cnt += m % (k + 1)

res = 0
res += cnt * ans1
res += (m - cnt) * ans2

print(res)