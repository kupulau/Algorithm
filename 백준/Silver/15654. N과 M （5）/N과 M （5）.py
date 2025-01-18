from itertools import permutations

n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()

list2 = permutations(list1, m)

for x in list2:
    print(*list(x))