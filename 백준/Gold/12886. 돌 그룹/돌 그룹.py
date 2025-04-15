from collections import deque

a, b, c = map(int, input().split())
total = a + b + c

if total%3 != 0:
    print(0)
    exit()
    
visited = set()
q = deque()

def add_state(x, y):
    z = total - x - y
    sorted_state = tuple(sorted([x, y, z]))
    if sorted_state not in visited:
        visited.add(sorted_state)
        q.append(sorted_state)
        
start = tuple(sorted([a, b, c]))
visited.add(start)
q.append(start)

while q:
    x, y, z= q.popleft()
    if x == y == z:
        print(1)
        break
    
    for u, v in ((x, y), (x, z), (y, z)):
        if u != v:
            if u < v:
                add_state(u+u, v-u)
                
            else:
                add_state(u-v, v+v)
                
else:   # while-else
    print(0)