import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and field[ny][nx] == 1:
                field[ny][nx] = 0
                q.append((ny, nx))      

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                BFS(j, i)
                cnt += 1                
    print(cnt)