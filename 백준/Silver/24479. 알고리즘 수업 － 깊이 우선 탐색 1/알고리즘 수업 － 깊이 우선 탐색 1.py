import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

no_points, no_lines, start = map(int, input().split())

graph = [[] for _ in range(no_points+1)]
visited = [0]*(no_points+1)    # 0이면 방문하지 않음

for i in range(no_lines):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# sort by ascending order
for i in range(no_points+1):
    graph[i].sort()

c = 1
def DFS(graph, start, visited):
    global c
    visited[start] = c
    
    for i in graph[start]:
        if visited[i] == 0:
            c += 1
            DFS(graph, i, visited)   # recursive DFS

DFS(graph, start, visited)

for i in range(1, no_points+1):
    print(visited[i])