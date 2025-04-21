from collections import deque

a, b = map(int, input().split())

q = deque()
q.append((b, 0))

visited = set()
visited.add(b)

found = False
while q:
    s, cnt = q.popleft()
    if s == a:
        print(cnt+1)
        found = True
        break
    
    if s%2 == 0:
        if 0 <= s/2 < b+1 and int(s/2) not in visited:
            visited.add(int(s/2))
            q.append((int(s/2), cnt+1))
            
    if (s-1)%10 == 0:
        if 0 <= (s-1)/10 < b+1 and int((s-1)%10) not in visited:
            visited.add(int((s-1)/10))
            q.append((int((s-1)/10), cnt+1))
            
if not found:
    print(-1)