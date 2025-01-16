from itertools import combinations

n, m = map(int, input().split())

list1 = [x+1 for x in range(n)]
list2 = list(combinations(list1, m))

for x in list2:
    print(*list(x))