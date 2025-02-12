import sys
input = sys.stdin.readline

k = int(input())

list1 = []
for _ in range(k):
    num = int(input())
    if num == 0:
        list1.pop()
    else:
        list1.append(num)

print(sum(list1))