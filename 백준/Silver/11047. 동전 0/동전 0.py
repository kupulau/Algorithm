import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
    
coins = [x for x in coins if x <= k]
coins.sort(reverse=True)

cnt = 0
for i in range(len(coins)):
    quotient, rest = k//coins[i], k%coins[i]
    cnt += quotient
    k -= quotient*coins[i]
    if rest == 0:
        break
    
print(cnt)