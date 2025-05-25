import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    list1 = list(map(int, input().split()))
    list1.sort()
    print(list1[0], list1[-1])