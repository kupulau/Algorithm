import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))    # cost, node 1, node 2
    
graph.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
result = 0
for cost, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)