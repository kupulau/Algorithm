import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))

dp = [0]*n
dp[0] = list1[0]

for i in range(1, n):
    for j in range(i):
        if list1[j] < list1[i]:
            dp[i] = max(dp[i], dp[j]+list1[i])
        else:
            dp[i] = max(dp[i], list1[i])

print(max(dp))