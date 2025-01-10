import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
