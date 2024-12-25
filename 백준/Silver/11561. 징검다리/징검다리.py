input1 = int(input())

for a in range(input1):
    stones = int(input())
    answer = 0
    left = 1
    right = stones
    while left <= right:
        mid = (left + right)//2
        if ((mid+1)*mid)//2 <= stones:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    print(answer)