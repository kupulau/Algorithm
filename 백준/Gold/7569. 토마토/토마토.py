import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())    # 가로, 세로, 높이

tomato = []
for i in range(h):
    list2 = []
    for j in range(n):
        list1 = list(map(int, input().split()))
        list2.append(list1)
    tomato.append(list2)
    
visited = [[[0]*(m) for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

answer = 0    # 처음부터 모든 토마토가 익어있는 상태

def BFS():
    while queue:
        x, y, z = queue.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            
            if tomato[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                visited[nx][ny][nz] = 1           

# 값이 1인 배열의 위치를 queue에 담음 -> 탐색해서 그 주위를 익히기 위해서
for a in range(h):
    for b in range(n):
        for c in range(m):
            if tomato[a][b][c] == 1 and visited[a][b][c] == 0:
                queue.append((a,b,c))
                visited[a][b][c] = 1

# 토마토 익히기
BFS()

# 토마토 확인
for a in tomato:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)    # 모든 토마토가 익지 못한 상태이므로
                exit(0)            
        answer = max(answer, max(b))     # 만약 처음부터 토마토가 다 익어있었다면 0을 반환

print(answer-1)   # day이므로