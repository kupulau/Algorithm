m, n = map(int, input().split())

eratosthenes = [False,False] + [True]*(n-1)

primes = []
for i in range(2, n+1):
    if eratosthenes[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            eratosthenes[j] = False

answer = [x for x in primes if x >= m]

for x in answer:
    print(x)