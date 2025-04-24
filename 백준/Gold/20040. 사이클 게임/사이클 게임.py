import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
    
parent = [i for i in range(n+1)]
    
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
graph = []
answer = 0
found = False
for _ in range(m):
    answer += 1
    a, b = map(int, input().split())
    graph.append((a, b))
    if find(a) != find(b):
        union(a, b)
    else:   # when the cycle is found
        print(answer)
        found = True
        break

if not found:
    print(0)