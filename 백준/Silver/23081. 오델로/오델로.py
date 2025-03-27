import sys
input = sys.stdin.readline

n = int(input())
board = [input().strip() for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def count_flip(board, x, y):
    total_flips = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        flip_count = 0
        while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'W':
            nx += dx
            ny += dy
            flip_count += 1
            
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'B':
            total_flips += flip_count
            
    return total_flips

results = []
for i in range(n):
    for j in range(n):
        if board[i][j] == ".":
            n_flip = count_flip(board, i, j)
            results.append((i, j, n_flip))

maxflip = max([x[2] for x in results]) 
answer = [x for x in results if x[2]==maxflip]
answer.sort(key=lambda x:(x[0], x[1]))

if maxflip == 0:
    print("PASS")
else:
    print(answer[0][1], answer[0][0])
    print(maxflip)