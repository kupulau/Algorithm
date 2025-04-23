import sys
input = sys.stdin.readline

n = int(input())

answer = 1    # initialization
for _ in range(n):
    a, b = map(int, input().split())
    if a != b:
        if a == answer:
            answer = b
        elif b == answer:
            answer = a
    
print(answer)