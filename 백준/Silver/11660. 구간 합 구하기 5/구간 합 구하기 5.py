import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tbl = [[0]*(n+1)]
for _ in range(n):
    list1 = [0] + list(map(int, input().split()))
    tbl.append(list1)
    
cum = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        cum[i][j] = tbl[i][j] + cum[i][j-1] + cum[i-1][j] - cum[i-1][j-1]
         
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = cum[x2][y2] - cum[x2][y1-1] - cum[x1-1][y2] + cum[x1-1][y1-1]
    print(answer)