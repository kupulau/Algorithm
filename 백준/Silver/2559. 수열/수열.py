import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperatures = list(map(int, input().split()))

cum = [sum(temperatures[:k])]
for i in range(0, n-k):
    sum1 = cum[i] - temperatures[i] + temperatures[k+i]
    cum.append(sum1)
    
print(max(cum))