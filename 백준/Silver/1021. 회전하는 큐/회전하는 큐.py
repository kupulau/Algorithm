import sys
from collections import deque 
input = sys.stdin.readline

n, m = map(int, input().split())
goal = list(map(int, input().split()))

list1 = deque([x+1 for x in range(n)])

def to_left(deque1):
    pop1 = deque1.popleft()
    deque1.append(pop1)
    return deque1
    
def to_right(deque1):
    pop1 = deque1.pop()
    deque1.appendleft(pop1)
    return deque1

cnt = 0
while len(goal) != 0:
    if list1[0] == goal[0]:
        list1.popleft()
        goal.remove(goal[0])
    else:
        idx = list1.index(goal[0])
        if idx > len(list1)//2:
            for _ in range(abs(idx-len(list1))):
                list1 = to_right(list1)
                cnt += 1
        else:
            for _ in range(idx):
                list1 = to_left(list1)
                cnt += 1
            
print(cnt)