#한 번 계산된 정보를 메모이제이션 하기 위한 리스트 초기화
d=[0]*100

def fibonacci(x):
  if x==1 or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  d[x]=fibonacci(x-1)+fibonacci(x-2)
  return d[x]

print(fibonacci(99))

#p.212 피보나치 수열(재귀)