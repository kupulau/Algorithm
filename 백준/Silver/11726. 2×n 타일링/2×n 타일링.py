n = int(input())

dp = [0]*n

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:   # n >= 3
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-2]+dp[i-1]        
    print(dp[-1]%10007)