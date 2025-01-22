import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for x in range(n+1)]
parents = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def BFS(start):
    queue = deque([start])
    parents[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if parents[i]==0:
                parents[i] = v
                queue.append(i)

BFS(1)

for i in range(2, n+1):
    print(parents[i])