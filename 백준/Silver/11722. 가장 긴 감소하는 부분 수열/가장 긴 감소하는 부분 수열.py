import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int,input().split()))

dp = [1] * n    # dp를 1로 초기화

for i in range(n):
    for j in range(0, i):
        if list1[i] < list1[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))