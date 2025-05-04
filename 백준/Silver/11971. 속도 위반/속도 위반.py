import sys
input = sys.stdin.readline

n, m = map(int, input().split())

limit = []
for _ in range(n):
    dist, speed = map(int, input().split())
    limit += [speed]*dist
    
yj = []
for _ in range(m):
    dist, speed = map(int, input().split())
    yj += [speed]*dist
    
maxspeeding = 0
i = 0
while i < 100:
    maxspeeding = max(maxspeeding, yj[i] - limit[i])
    i += 1
    
print(maxspeeding)