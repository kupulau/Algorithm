import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)

cost = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    cost += (a+b)
    heapq.heappush(card, a+b)
    
print(cost)