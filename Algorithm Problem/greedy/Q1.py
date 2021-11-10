N=int(input())

data=list(map(int, input().split()))
data.sort()

result=0
count=0

for i in data:
  count+=1
  if count>=i:
    result+=1
    count=0

print(result)

#p.311 모험가 길드