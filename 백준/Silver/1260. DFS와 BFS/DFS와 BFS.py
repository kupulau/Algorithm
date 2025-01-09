from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, start = map(int, input().split())

visited = [False]*(n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:   # sort by ascending order
    i.sort()

def DFS(start):
    visited[start] = True
    print(start, end=" ")
    
    for i in graph[start]:
        if not visited[i]:
            DFS(i)
    
def BFS(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

DFS(start)
print()
visited = [False]*(n+1)
BFS(start)
