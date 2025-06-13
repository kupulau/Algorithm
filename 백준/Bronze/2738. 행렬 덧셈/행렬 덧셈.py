n, m = map(int, input().split())

matA = []
for _ in range(n):
    list1 = list(map(int, input().split()))
    matA.append(list1)

matB = []
for _ in range(n):
    list1 = list(map(int, input().split()))
    matB.append(list1)
    
matsum = []
for i in range(n):
    matsum.append([a+b for a, b in zip(matA[i], matB[i])])
    
for i in range(n):
    print(*matsum[i])