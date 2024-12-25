import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    
s = int(input())

fan = list(map(int, input().split()))

visited = [0]*(n+1)

# 팬클럽 곰곰이가 있는 노드는 방문 처리
for i in fan:
    visited[i] = 1
    
def BFS(graph, start):
    q = deque([start])
    if visited[start]:
        return 'Yes'
    visited[start] = 1
    while q:
        now = q.popleft()
        if not graph[now]:
            return 'yes'
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    return 'Yes'

print(BFS(graph, 1))