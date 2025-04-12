import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

good = 0
for i in range(n):      
    x = nums[i]    # 인덱스로 하는 이유 : 같은 숫자라도 다른 위치에 있다면 다른 수로 간주한다고 했기 때문
    left = 0
    right = n-1
    while left < right:
        if i == left:
            left += 1
            continue
        if i == right:
            right -= 1
            continue

        sum1 = nums[left] + nums[right]
        if sum1 == x:
            good += 1
            break
        elif sum1 > x:
            right -= 1
        else:    # sum1 < x
            left += 1

print(good)