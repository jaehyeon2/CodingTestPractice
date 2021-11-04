n=int(input())
array=[0]*100001

for i in input().split():
  array[int(i)]=1

m=int(input())
target_array=list(map(int, input().split()))

for i in target_array:
  if array[i]==1:
    print("yes", end=" ")
  else:
    print("no", end=" ")
print(end="\n")

#p.199 부품 찾기(계수 정렬)