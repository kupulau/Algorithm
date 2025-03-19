n = int(input())

# dp[i][j] : 길이가 i이고 마지막 숫자가 j인 계단 수의 개수
dp = [[0]*10 for _ in range(n+1)]

for j in range(1, 10):    # N = 1일 때 1~9 초기화
    dp[1][j] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:     # 끝자리가 0이면 1밖에 붙일 수 없음
            dp[i][j] = dp[i-1][1]
        elif j == 9:  # 끝자리가 9이면 8밖에 붙일 수 없음  
            dp[i][j] = dp[i-1][8]
        else:   # 그 외에는 j-1, j+1의 수를 붙일 수 있음
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%1000000000  
            
print(sum(dp[n])%1000000000)