from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [0 for _ in range(100001)]

cnt, result = 0, 0

while q:
    s = q.popleft()
    temp = visited[s]
    if s == k:
        result = temp
        cnt += 1
        continue
    for i in [s-1, s+1, 2*s]:
        if 0 <= i < 100001 and (visited[i]==0 or visited[i]==visited[s]+1):      # 같은 최소 시간으로 도달하는 경우: 경우의 수 누적
            visited[i] = visited[s]+1
            q.append(i)

print(result)
print(cnt)      