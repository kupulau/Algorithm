import sys
input = sys.stdin.readline

n = int(input())
blob = list(map(int, input().split()))

if n == 1:
    print(blob[0])
elif n == 2:
    print(max(blob))
else:     # n >= 3
    max1 = max(blob)
    for i in range(1, n-1):   
        if blob[i-1] >= 1 and blob[i+1] >= 1:
            current = blob[i] + min(blob[i-1], blob[i+1])
            if current > max1:
                max1 = current
                
    print(max1)