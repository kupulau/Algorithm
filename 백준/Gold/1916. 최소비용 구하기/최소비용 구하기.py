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
    distances = [1e9]*(n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if distances[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
                
    return distances

answer = dijkstra(graph, start)
print(answer[goal])