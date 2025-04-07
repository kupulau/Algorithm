import sys
import heapq
input = sys.stdin.readline

n = int(input())   
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    
start, goal = map(int, input().split())

def dijkstra(graph, start):
    cost = [float('inf')]*(n+1)
    cost[start] = 0
    prev = [0]*(n+1)
    q = []
    heapq.heappush(q, [cost[start], start])
    while q:
        c, node = heapq.heappop(q)
        if cost[node] < c:
            continue
        for next_node, next_cost in graph[node]:
            co = c + next_cost
            if co < cost[next_node]:
                cost[next_node] = co
                heapq.heappush(q, [co, next_node])
                prev[next_node] = node
                
    return cost, prev
    
cost, prev = dijkstra(graph, start)

# route backtracking
route = []
current = goal
while current:
    route.append(current)
    current = prev[current]
route.reverse()

print(cost[goal])
print(len(route))
print(*route)