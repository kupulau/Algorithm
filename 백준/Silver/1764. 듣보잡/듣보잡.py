import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list1 = {}
for _ in range(n):
    list1[input().rstrip()] = 1
    
list2 = []
for _ in range(m):
    name = input().rstrip()
    if name in list1:
        list2.append(name)
    
list2.sort()
print(len(list2))
for x in list2:
    print(x)