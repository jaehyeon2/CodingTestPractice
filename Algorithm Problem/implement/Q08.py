STR=input()
string=[]
sum=0

for i in STR:
  if i.isalpha():
    string.append(i)
  else:
    sum+=int(i)

string.sort()
if sum!=0:
  string.append(str(sum))
print(''.join(string))

#p.322 문자열 재정렬