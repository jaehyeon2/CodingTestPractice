data=input()

result=0
for i in range(len(data)):
  result=max(result+int(data[i]), result*int(data[i]))

print(result)

#p.312 곱하기 혹은 더하기