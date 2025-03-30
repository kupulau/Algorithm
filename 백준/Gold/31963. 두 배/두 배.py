import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))

cnt = 0
for i in range(len(list1)-1):
    a = list1[i]
    b = list1[i+1]
    if a <= b:
        pass
    else:
        while a > b:
            b = 2*b
            cnt += 1
        list1[i+1] = b

print(cnt)