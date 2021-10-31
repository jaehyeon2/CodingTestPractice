from collections import deque

queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)      #순서대로 출력
queue.reverse()   #queue 역순으로 바꾸기
print(queue)

#p.129 큐 예제