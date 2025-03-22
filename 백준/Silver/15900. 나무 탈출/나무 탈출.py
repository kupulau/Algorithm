import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
total_moves = 0  # 총 이동 횟수

def DFS(node, depth):
    global total_moves
    visited[node] = True
    is_leaf = True  # 현재 노드가 리프인지 확인

    for next_node in graph[node]:
        if not visited[next_node]:
            is_leaf = False
            DFS(next_node, depth + 1)

    if is_leaf:  # 리프 노드일 경우에만 depth를 더함
        total_moves += depth

# 루트(1)에서 DFS 탐색 시작
DFS(1, 0)

# 이동 횟수가 홀수면 성원이 승, 짝수면 형석이 승
print("Yes" if total_moves % 2 == 1 else "No")