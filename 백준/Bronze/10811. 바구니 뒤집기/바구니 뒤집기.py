import sys
input = sys.stdin.readline

n, m = map(int, input().split())
baskets = [x+1 for x in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    part1 = baskets[:a]
    part2 = baskets[a:b+1][::-1]
    part3 = baskets[b+1:]
    baskets = part1 + part2 + part3
    
print(*baskets)