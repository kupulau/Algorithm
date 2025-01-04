import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list1 = list(map(int, input().split()))

sum1 = [0]
c = 0
for x in list1:
    c += x
    sum1.append(c)

for _ in range(m):
    a, b = map(int, input().split())
    print(sum1[b]-sum1[a-1])