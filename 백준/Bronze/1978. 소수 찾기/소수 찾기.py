n = int(input())
list1 = list(map(int, input().split()))
max1 = max(list1)

eratosthenes = [False, False] + [True]*(max1-1)
primes = []
for i in range(2, max1+1):
    if eratosthenes[i]:
        primes.append(i)
        for j in range(2*i, max1+1, i):
            eratosthenes[j] = False
            
answer = [x for x in list1 if x in primes]
print(len(answer))