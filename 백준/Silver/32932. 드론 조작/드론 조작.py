import sys
input = sys.stdin.readline

n, k = map(int, input().split())
obstacles = [list(map(int, input().split())) for _ in range(n)]
moves = input().strip()
drone = [0, 0]

for i in range(k):
    dx, dy = 0, 0
    if moves[i] == 'U':
        dy = 1
        
    elif moves[i] == 'D':
        dy = -1
        
    elif moves[i] == 'L':
        dx = -1
        
    elif moves[i] == 'R':
        dx = 1
    
    nx, ny = drone[0]+dx, drone[1]+dy
    
    if [nx, ny] not in obstacles:
        drone = [nx, ny]
    
print(*drone) 