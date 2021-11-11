N=input()

length=len(N)
left=0
right=0
for i in range(length):
  if i<length//2:
    left+=int(N[i])
  else:
    right+=int(N[i])

if left==right:
  print("LUCKY")
else:
  print("READY")

#p.321 럭키 스트레이트