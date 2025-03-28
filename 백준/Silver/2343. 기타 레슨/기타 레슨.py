import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lectures = list(map(int, input().split()))

left = max(lectures)
right = sum(lectures)  

while left <= right:
    mid = (left + right)//2
    sum1 = 0
    cnt = 1
    for x in lectures:
        if sum1 + x > mid:
            cnt += 1
            sum1 = x
        else:
            sum1 += x
    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)