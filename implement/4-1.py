n=int(input())
x,y=1,1
plans=input().split()

#방향 이동 L, R, U, D
dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]
move_types=['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_types)):
    if plan==move_types[i]:
      nx=x+dx[i]
      ny=y+dy[i]
  #범위와 좌표 확인
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  # 이동 수행
  x, y=nx, ny

print(x, y)
#p.110 상하좌우