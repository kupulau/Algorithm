import sys
input = sys.stdin.readline

padovan = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for x in range(11, 101):
    padovan.append(padovan[x-2]+padovan[x-3])

n = int(input())
for i in range(n):
    m = int(input())
    print(padovan[m])