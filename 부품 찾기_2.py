n = int(input())
arr = set(map(int, input().split()))

m = int(input())
k = list(map(int, input().split()))

for i in k:
  if i in arr:
    print('yes', end = ' ')
  
  else:
    print('no', end = ' ')