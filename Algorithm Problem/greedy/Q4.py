n=int(input())
coin=list(map(int, input().split()))
coin.sort()

target=1
for i in coin:
  if target<i:
    break
  else:
    target+=i

print(target)

#p.314 만들 수 없는 금액