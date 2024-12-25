import sys
from collections import deque
input = sys.stdin.readline

def BFS(queue, visited, start, goal, dx, dy):
    queue.append(start)
    visited[start[0]][start[1]]
    
    while queue:
        x, y = queue.popleft()
        
        if x == goal[0] and y == goal[1]:
            return 0
        
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            
            if nx == goal[0] and ny == goal[1]:
                visited[nx][ny] == True
                return chess[x][y]+1
            
            if visited[nx][ny] == False:
                queue.append([nx, ny])
                visited[nx][ny] = True
                chess[nx][ny] = chess[x][y]+1
                

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, 2, 1, -1, -2]


n = int(input())

for i in range(n):
    size = int(input())
    start = list(map(int, input().split())) 
    goal = list(map(int, input().split()))
    
    chess = [[0]*size for _ in range(size)]
    visited = [[False]*size for _ in range(size)]
    
    queue = deque()
    
    answer = BFS(queue, visited, start, goal, dx, dy)
    
    print(answer)