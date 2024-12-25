import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
answer = 0

while left <= right:
    mid = (left + right)//2
    total_length = sum([x-mid for x in trees if x>mid])
    if total_length >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(answer)