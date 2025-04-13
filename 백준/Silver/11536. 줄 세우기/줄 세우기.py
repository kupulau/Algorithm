n = int(input())
name = [input() for _ in range(n)]
if name == sorted(name, reverse=True):
    print('DECREASING')
elif name == sorted(name, reverse=False):
    print('INCREASING')
else:
    print('NEITHER')