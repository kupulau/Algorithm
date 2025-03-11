import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    input1 = int(input())
    if input1 == 0:
        if len(heap)==0:
            print(0)
        else:
            out = heapq.heappop(heap)
            print(out[1])
        
    else:
        heapq.heappush(heap, (abs(input1), input1))