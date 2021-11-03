n= int(input())

array=[]
for i in range(n):
  array.append(int(input()))

array=sorted(array, reverse=True)

for i in array:
  print(i, end=" ")

#p.178 위에서 아래로