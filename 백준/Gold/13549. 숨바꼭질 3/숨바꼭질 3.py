from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1]==-1:
        visited[s-1] = visited[s] + 1
        q.append(s-1)
        
    if 0 < 2*s < 100001 and visited[2*s]==-1:       
        visited[2*s] = visited[s] + 0
        q.appendleft(2*s)    # priority
        
    if 0 < s+1 < 100001 and visited[s+1]==-1:
        visited[s+1] = visited[s] + 1
        q.append(s+1)