import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

def is_possible(distance):
    count = 1  # 첫 번째 집에 설치
    last_location = house[0]
    for i in range(1, n):
        if house[i] - last_location >= distance:
            count += 1
            last_location = house[i]
    return count # >= c

left = 1
right = house[-1] - house[0]
answer = 0
while left <= right:
    mid = (left + right)//2
    if is_possible(mid) >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
    
print(answer)   