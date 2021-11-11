data=input()
group=0

for i in range(1, len(data)):
  if(data[i-1]!=data[i]):
    group+=1

print(group//2)

#p.313 문자열 뒤집기