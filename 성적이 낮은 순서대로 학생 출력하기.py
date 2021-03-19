n = int(input())
arr = []

for i in range(n):
  arr.append(input().split())

arr = sorted(arr, key = lambda a : a[1])

for a in arr:
  print(a[0], end = ' ')