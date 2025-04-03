import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
 
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

answer = dijkstra(graph, start)
for i in range(1, n+1):
    if answer[i] == float('inf'):
        print('INF')
    else:
        print(answer[i]) 