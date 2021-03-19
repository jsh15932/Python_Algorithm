n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
k = list(map(int, input().split()))

def search(start, end, target, arr):
  if start > end:
    return None
  
  mid = (start + end) // 2

  if target == arr[mid]:
    return mid
  
  elif target > arr[mid]:
    return search(mid + 1, end, target, arr)

  else:
    return search(start, mid - 1, target, arr)

for i in k:
  res = search(0, n - 1, i, arr)

  if res == None:
    print('no', end = ' ')

  else:
    print('yes', end = ' ')