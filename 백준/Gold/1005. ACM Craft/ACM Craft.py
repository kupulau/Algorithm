import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    goal = int(input())
    
    # 건설 시간 기록
    answer = [0]*(n+1)
    q = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
            answer[i] = times[i-1]
            
    while q:
        now = q.popleft()
        for next in graph[now]:
            indegree[next] -= 1
            answer[next] = max(answer[next], answer[now]+times[next-1])
            if indegree[next] == 0:
                q.append(next)
                
    print(answer[goal])