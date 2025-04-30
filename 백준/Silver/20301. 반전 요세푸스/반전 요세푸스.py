from collections import deque

n, k, m = map(int, input().split())
q = deque(x+1 for x in range(n))

answer = []
cnt = 0 
direction = 1    # default direction
while q:
    if direction == 1:
        for _ in range(k-1):
            q.append(q.popleft())
        answer.append(q.popleft())
    else:
        for _ in range(k-1):
            q.appendleft(q.pop())
        answer.append(q.pop())
        
    cnt += 1
    if cnt%m == 0:
        direction *= -1     # reverse
        
for x in answer:
    print(x)