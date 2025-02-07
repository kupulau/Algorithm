import sys
input = sys.stdin.readline

n = int(input())

coords = []
for _ in range(n):
    a, b = map(int, input().split())
    coords.append([a,b])
    
coords.sort(key=lambda x:(x[0], x[1]))

for c in coords:
    print(*c)