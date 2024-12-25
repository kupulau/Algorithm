import sys
input = sys.stdin.readline

n = int(input())

kids = []
for _ in range(n):
    kids.append(int(input()))
    
dp = [1]*n

for i in range(len(kids)):
    for j in range(0, i):
        if kids[i] > kids[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))