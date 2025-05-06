import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

same = False
if a == b:
    print(1)
    exit()

for i in range(n-1, 0, -1):
    max_position = 0
    for j in range(1, i+1):
        if a[j] > a[max_position]:
            max_position = j
    a[i], a[max_position] = a[max_position], a[i] 
    
    if a == b:
        print(1)
        same = True
        break

if not same:
    print(0)