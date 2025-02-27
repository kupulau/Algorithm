import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))
   
left = 1
right = max(lines)
answer = []
while left <= right:
    mid = (left+right)//2
    num = sum([x//mid for x in lines])
    if num >= n:
        answer.append(mid)
        left = mid + 1
    else:
        right = mid - 1
        
print(max(answer))  