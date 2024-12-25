import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    for j in range(0, i):
        if size[i] > size[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))