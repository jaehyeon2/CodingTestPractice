spot=input()
row=int(spot[1])
col=int(ord(spot[0]))-int(ord('a'))+1

steps=[(2, 1),(2, -1),(1, 2),(1, -2),(-1, 2),(-1, -2),(-2, 1),(-2, -1)]

count=0
for step in steps:
  n_row=row+step[0]
  n_col=col+step[1]
  if n_row>=1 and n_row<=8 and n_col>=1 and n_col<=8:
    count+=1

print(count)

#p.115 왕실의 나이트