import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    func = input().strip()
    n = int(input())
    list1 = input().strip()
    
    if list1 == "[]":
        list1 = deque()
    else:
        list1 = deque(map(int, list1[1:-1].split(',')))
        
    reverse = 0      # 0, 2, 4, ... -> default / 1, 3, 5, ... -> reverse
    error = False
    for i in func:
        if i == 'R':
            reverse += 1
        elif i == 'D':
            if len(list1)==0:
                print('error')
                error = True
                break
            else:
                if reverse%2 == 0:
                    list1.popleft()
                else:
                    list1.pop()
    if not error:
        if reverse%2==1:
            list1.reverse()
            print('[' + ','.join(map(str, list1)) + ']')
        else:
            print('[' + ','.join(map(str, list1)) + ']')