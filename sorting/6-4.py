array=[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start>=end:    #원소가 1개인 경우 종료
    return
  pivot=start       #pivot은 첫번째 원소
  left=start+1
  right=end
  while left<=right:
    #pivot보다 큰 데이터를 찾을 때까지 반복
    while left<=end and array[left]<=array[pivot]:
      left+=1
    #pivot보다 작은 데이터를 찾을 때까지 반복
    while right>start and array[right]>=array[pivot]:
      right-=1
    #엇갈렸을 경우
    if left>right:
      array[right], array[pivot]=array[pivot], array[right]
    #아닐 경우
    else:
      array[left], array[right]=array[right], array[left]
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

#p.168 퀵 정렬