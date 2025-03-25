import sys
input = sys.stdin.readline

n, m = map(int, input().split())

space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

inf = float('inf')   
dp = [[[inf]*3 for _ in range(m)] for _ in range(n)]

# 첫째 행 초기화
for j in range(m):   
    for d in range(3):    # direction
        dp[0][j][d] = space[0][j]

# 우주 탐험
for i in range(1, n):
    for j in range(m):
        # 왼쪽 위에서 오는 경우 (j-1 -> j)
        if j > 0:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + space[i][j]
        
        # 바로 위에서 오는 경우 (j -> j)
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + space[i][j]
        
        # 오른쪽 위에서 오는 경우 (j+1 -> j)
        if j < m-1:
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + space[i][j]
            
# 정답
answer = inf
for j in range(m):
    answer = min(answer, min(dp[n-1][j]))
    
print(answer)