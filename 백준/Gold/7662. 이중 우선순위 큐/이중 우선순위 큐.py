import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    minq, maxq = [], []
    count = [False]*k
    for i in range(k):
        operator, x = input().strip().split()
        x = int(x)
        if operator == 'I':
            heapq.heappush(minq, (x, i))
            heapq.heappush(maxq, (-x, i))
            count[i] = True
        else:    # operator == 'D'
            if x == -1:
                if len(minq) > 0:
                    val = heapq.heappop(minq)[1]
                    count[val] = False
            else:   # value == 1
                if len(maxq) > 0:
                    val = heapq.heappop(maxq)[1]
                    count[val] = False
                
        while minq and count[minq[0][1]] == False:
            heapq.heappop(minq)
            
        while maxq and count[maxq[0][1]] == False:
            heapq.heappop(maxq)

    if minq == []:
        print("EMPTY")         
    else:
        print(-maxq[0][0], minq[0][0])  