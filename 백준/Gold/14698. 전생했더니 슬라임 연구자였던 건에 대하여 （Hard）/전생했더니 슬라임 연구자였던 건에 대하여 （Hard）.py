import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    slimes = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        heapq.heapify(slimes)
        cost = 1
        while len(slimes) > 1:
            a = heapq.heappop(slimes)
            b = heapq.heappop(slimes)
            cost *= (a*b)
            heapq.heappush(slimes, a*b)
            
        print(cost%1000000007)