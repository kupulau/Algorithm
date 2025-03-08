import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    cards.sort()
    new = cards[0]+cards[1]
    cards[0], cards[1] = new, new
    
print(sum(cards))