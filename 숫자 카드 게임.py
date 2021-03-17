n, m = map(int, input().split())
res = 0

for i in range(n):
    data = list(map(int, input().split()))
    ans = min(data)
    res = max(res, ans)

print(res)