from itertools import permutations

n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()

list2 = permutations(list1, m)
list2 = list(set(list2))
list2.sort()

for x in list2:
    print(*list(x))