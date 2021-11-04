def binary_search(array, target, start, end):
  while start<=end:
    mid=(start+end)//2
    if target==array[mid]:
      return True
    elif target<array[mid]:
      return binary_search(array, target, start, mid-1)
    else:
      return binary_search(array, target, mid+1, end)
  return False

n=int(input())
array=list(map(int, input().split()))
array.sort()

m=int(input())
target_array=list(map(int, input().split()))

for i in target_array:
  result=binary_search(array, i, 0, n-1)
  if result==True:
    print("yes", end=" ")
  else:
    print("no", end=" ")
print("\n")

#p.198 부품 찾기(이진 탐색)