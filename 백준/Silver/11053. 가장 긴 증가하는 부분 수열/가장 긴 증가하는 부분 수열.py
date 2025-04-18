import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if list1[j] < list1[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))