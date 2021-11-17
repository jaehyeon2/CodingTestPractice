from collections import deque
n, m, k, x=map(int, input().split())
road=[[]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b=map(int, input().split())
  road[a].append(b)

distance=[-1]*(n+1)
distance[x]=0

q=deque([x])
while q:
  now=q.popleft()
  for node in road[now]:
    if distance[node]==-1:
      distance[node]=distance[now]+1
      q.append(node)

check=False
for i in range(1, n+1):
  if distance[i]==k:
    print(i)
    check=True

if check==False:
  print(-1)
