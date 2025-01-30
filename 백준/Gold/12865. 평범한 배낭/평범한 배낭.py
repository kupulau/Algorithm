import sys
input = sys.stdin.readline

n, k = map(int, input().split())     # number of things, limit weight

list1 = []
for _ in range(n):
    list1.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if list1[i-1][0] <= j:
            dp[i][j] = max(list1[i-1][1]+dp[i-1][j - list1[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[n][k])