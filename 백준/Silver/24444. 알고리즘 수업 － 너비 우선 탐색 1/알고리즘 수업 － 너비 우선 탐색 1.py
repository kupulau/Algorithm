from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort(reverse=False)

cnt = 1
def BFS(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = cnt
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = cnt
    
BFS(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])