from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [-1 for _ in range(100001)]    # 해당 숫자에 도착하는 시간을 저장
visited[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    
    for i in [s-1, s+1, 2*s]:
        if 0 <= i < 100001 and visited[i]==-1:
            visited[i] = visited[s]+1
            q.append(i)