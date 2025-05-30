import sys
input = sys.stdin.readline

n = int(input())

chang = 100
sang = 100
for _ in range(n):
    c, s = map(int, input().split())
    if c == s:
        pass
    elif c > s:
        sang -= c
    else:    # c < s
        chang -= s
    
print(chang)
print(sang)