import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())   # 가로, 세로
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if tomato[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append((ny, nx))
                tomato[ny][nx] = tomato[y][x] + 1
                visited[ny][nx] = 1
    
# 값이 1인 배열의 위치를 queue에 담음 -> 탐색해서 그 주위를 익히기 위해서
for a in range(n):
    for b in range(m):
        if tomato[a][b] == 1 and visited[a][b] == 0:
            q.append((a, b))
            visited[a][b] = 1

# 토마토 익히기
BFS()

# 토마토 확인
answer = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)    # 모든 토마토가 익지 못한 상태이므로
            exit(0)            
        answer = max(answer, tomato[i][j])     # 만약 처음부터 토마토가 다 익어있었다면 0을 반환

print(answer-1)   # day이므로