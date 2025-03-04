import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
   
def BFS(start, goal):
    visited = [0]*(n+1)
    q = deque([(start, 0)])
    visited[start] = 1
    while q:
        now, distance = q.popleft()
        
        if now == goal:
            return distance
        
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i, distance+1))
                
KB = []
for i in range(1, n+1):
    sum1 = 0
    for j in range(1, n+1):
        sum1 += BFS(i, j)
    KB.append(sum1)

min1 = min(KB)
print(KB.index(min1)+1)