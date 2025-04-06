import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
v1, v2 = map(int, input().split())

def dijkstra(graph, start):
    distances = [float('inf')]*(n+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    while q:
        dist, node = heapq.heappop(q)
        if distances[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(q, [distance, next_node])
                
    return distances
    
answer1 = dijkstra(graph, 1)
answer2 = dijkstra(graph, v1)
answer3 = dijkstra(graph, v2)

# (1) 1 -> v1 -> v2 -> n
# (2) 1 -> v2 -> v1 -> n
answer = min(answer1[v1]+answer2[v2]+answer3[-1], answer1[v2]+answer3[v1]+answer2[-1])

if answer == float('inf'):
    print(-1)
else:
    print(answer)