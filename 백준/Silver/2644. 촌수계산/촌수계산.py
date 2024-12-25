import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())   # 전체 사람 수
a, b = map(int, input().split())    # a와 b는 몇 촌?
visited = [0]*(n+1)

m = int(input())   
graph = [[] for _ in range(n+1)]

for i in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)    

result = []

def DFS(graph, start, goal, depth):
    depth += 1
    visited[start] = 1
    
    if start == goal:
        result.append(depth)
        
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, goal, depth)
            
DFS(graph, a, b, 0)

if len(result) == 0:
    print(-1)

else:
    print(result[0]-1)