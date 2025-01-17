from itertools import combinations_with_replacement

n, m = map(int, input().split())

list1 = [x+1 for x in range(n)]
list2 = combinations_with_replacement(list1, m)

for x in list2:
    print(*list(x))