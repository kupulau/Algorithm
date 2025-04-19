import heapq
from collections import defaultdict

def insert(x):
    heapq.heappush(minq, x)
    heapq.heappush(maxq, -x)
    count[x] += 1
    
def delete_min():
    while minq:
        val = heapq.heappop(minq)
        if count[val] > 0:
            count[val] -= 1
            break

def delete_max():
    while maxq:
        val = -heapq.heappop(maxq)
        if count[val] > 0:
            count[val] -= 1
            break

t = int(input())
for _ in range(t):
    k = int(input())
    minq, maxq = [], []
    count = defaultdict(int)
    for _ in range(k):
        operator, value = input().split()
        if operator == 'I':
            insert(int(value))
        else:
            if value == '-1':
                delete_min()
            else:
                delete_max()
                
    answer = [x for x in count if count[x]>0]
    if len(answer)==0:
        print('EMPTY')
    else:
        print(max(answer), min(answer))