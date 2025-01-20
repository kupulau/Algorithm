from itertools import combinations_with_replacement

n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()

list2 = combinations_with_replacement(list1, m)
list2 = list(set(list2))
list2.sort()

for x in list2:
    print(*list(x))