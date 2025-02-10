from collections import deque

n = int(input())

q = deque(x+1 for x in range(n))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])