from collections import deque

n, k=map(int, input().split())
board=[]
data=[]
temp=[]
for i in range(n):
  board.append(list(map(int, input().split())))
  for j in range(n):
    if board[i][j]!=0:
      data.append((board[i][j], i, j))

data.sort()
q=deque(data)
temp=deque()

dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]

s, x, y=map(int, input().split())

for i in range(s):
  while q:
    now_v, now_x, now_y=q.popleft()
    for i in range(4):
      nx=now_x+dx[i]
      ny=now_y+dy[i]
      
      if nx>=n or ny>=n or nx<0 or ny<0:
        continue
      if board[nx][ny]==0:
        board[nx][ny]=now_v
        
        temp.append((now_v, nx, ny))
  q=temp

print(board[x-1][y-1])