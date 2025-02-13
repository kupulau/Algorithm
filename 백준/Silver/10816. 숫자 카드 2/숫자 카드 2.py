import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

dict1 = {}
for x in list1:
    if x in dict1.keys():
        dict1[x] += 1
    else:
        dict1[x] = 1

for x in list2:
    if x in dict1.keys():
        print(dict1[x], end=' ')
    else:
        print(0, end=' ')