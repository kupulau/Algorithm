import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(graph, start):
    times = [float('inf')]*(n+1)     
    times[start] = 0
    q = []
    heapq.heappush(q, [times[start], start])
    while q:
        t, node = heapq.heappop(q)
        if times[node] < t:
            continue
        for next_node, next_time in graph[node]:
            time = t + next_time
            if time < times[next_node]:
                times[next_node] = time
                heapq.heappush(q, [time, next_node])
    return times
    
# come back home
home = dijkstra(graph, x)

# to the party
party = [0]    # 0th index is dummy data
for i in range(1, n+1):
    p = dijkstra(graph, i)
    party.append(p[x])
    
answer = [x+y for x, y in zip(home, party) if x + y != float('inf')]
print(max(answer))