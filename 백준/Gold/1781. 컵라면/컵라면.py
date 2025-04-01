import sys
import heapq
input = sys.stdin.readline

n = int(input())
ramen = []
for _ in range(n):
    ramen.append(tuple(map(int, input().split())))
    
ramen.sort()

answer = []
heapq.heapify(answer)
for day, ram in ramen:
    heapq.heappush(answer,ram)
    if len(answer) > day:
        heapq.heappop(answer)

print(sum(answer))