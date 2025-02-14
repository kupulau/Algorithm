from collections import deque

n, k = map(int, input().split())

q = deque(x+1 for x in range(n))

answer = []
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())

answer = [str(x) for x in answer]
answer = ', '.join(answer)
print('<'+answer+'>')