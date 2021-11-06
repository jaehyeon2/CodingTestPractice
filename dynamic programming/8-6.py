n=int(input())
k=list(map(int, input().split()))

d=[0]*100

d[0]=k[0]
d[1]=max(k[0], k[1])

for i in range(2, n):
  d[i]=max(d[i-2]+k[i], d[i-1])

print(d[n-1])

#p.220 개미 전사