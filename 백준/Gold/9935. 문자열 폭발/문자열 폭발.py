import sys
input = sys.stdin.readline

string = input().strip()
explode = input().strip()
L = len(explode)

stack = []
for s in string:
    stack.append(s)
    if ''.join(stack[-L:])==explode:
        del stack[-L:]

answer = ''.join(stack)

if len(answer)==0:
    print('FRULA')
else:
    print(answer)