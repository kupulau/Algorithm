import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
distance = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)    # one-way?
    
def BFS(start, goal):
    answer = []
    q = deque([start])
    visited[start] = 1
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i]==0:
                visited[i] = 1
                q.append(i)
                distance[i] = distance[now]+1
                if distance[i] == goal:
                    answer.append(i)
                    
    answer.sort()                
    
    if len(answer) == 0:
        print(-1)
    else:
        for i in answer:
            print(i)
        
BFS(x, k)  