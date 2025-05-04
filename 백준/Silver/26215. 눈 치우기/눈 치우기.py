import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))

cnt = 0

if n == 1:
    cnt += list1[0]
else:
    while sum(list1) != 0:
        list1.sort(reverse=True)
        if list1[0] != 0 and list1[1] != 0:
            cnt += list1[1]
            list1[0] -= list1[1]
            list1[1] = 0
        else:
            cnt += list1[0]
            list1[0] = 0
    
if cnt > 1440:
    print(-1)
else:
    print(cnt)