import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))
list2 = list(set(list1))
list2.sort()

dict = {v: k for k, v in enumerate(list2)}

for x in list1:
    print(dict[x], end=" ")