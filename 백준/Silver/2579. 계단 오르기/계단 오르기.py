#import sys
#input = sys.stdin.readline

n = int(input())

stairs = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(stairs))
else:    # n >= 3
    dp = [0]*n 
    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
    print(dp[-1])