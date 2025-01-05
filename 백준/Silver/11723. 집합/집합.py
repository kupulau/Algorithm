import sys
input = sys.stdin.readline

m = int(input())
S = set()

for _ in range(m):
    c = input().split()
    if c[0] == 'add':
        if int(c[1]) in S:
            pass
        else:
            S.add(int(c[1]))
    elif c[0] == 'remove':
        if int(c[1]) not in S:
            pass
        else:
            S.discard(int(c[1]))
    elif c[0] == 'check':
        if int(c[1]) in S:
            print(1)
        else:
            print(0)
    elif c[0] == 'toggle':
        if int(c[1]) in S:
            S.discard(int(c[1]))
        else:
            S.add(int(c[1]))
    elif c[0] == 'all':
        S = set([x+1 for x in range(20)])
    elif c[0] == 'empty':
        S = set()