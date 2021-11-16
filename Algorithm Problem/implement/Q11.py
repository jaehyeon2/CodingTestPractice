from collections import deque

n=int(input())
k=int(input())

board=[[0]*(n+1) for _ in range(n+1)]
direction=0
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
timing=[0]*100
time=0
queue=deque()
queue.append((0, 0))
x, y=0, 0
board[0][0]=2
for i in range(k):
  row, col=map(int, input().split())
  board[row-1][col-1]=1

l=int(input())
for _ in range(l):
  temp1, temp2=input().split()
  if temp2=="L":
    turn=-1
  else:
    turn=1
  timing[int(temp1)]=turn

while(True):
  time+=1
  x+=dx[direction]
  y+=dy[direction]
  if x>=n or y>=n or x<0 or y<0:
    print(board[0][1])
    break
  if board[x][y]==2:
    break
  queue.append((x, y))
  print(x, y)
  board[x][y]=2
  print(board[x][y])
  direction=(direction+timing[time])%4
  if board[x][y]==1:
    continue
  tail=queue.popleft()
  board[tail[0]][tail[1]]=0
  

print(time)