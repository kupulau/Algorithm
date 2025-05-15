import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = input().split()
    c = int(a, 2) + int(b, 2)
    c = bin(c)
    print(int(c[2:]))