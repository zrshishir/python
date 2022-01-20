from collections import deque

queue = deque(['a', 'b', 'c', 'd', 'e'])
print(queue)

queue.append('f')
print(queue)

queue.appendleft('1')
print(queue)

queue.pop()
print(queue)

queue.popleft()
print(queue)