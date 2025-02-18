import sys
input = sys.stdin.readline

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

answer1 = [x//t+1 if x%t!=0 else x//t for x in sizes]

print(sum(answer1))
print(n//p, n%p)