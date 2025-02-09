import sys
input = sys.stdin.readline

n = int(input())
list1 = set(map(int, input().split()))

m = int(input())
list2 = list(map(int, input().split()))

for i in range(m):
    if list2[i] in list1:
        print(1)
    else:
        print(0)