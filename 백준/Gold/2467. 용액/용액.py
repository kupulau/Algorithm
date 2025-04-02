import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

left = 0
right = n-1

min1 = float('inf')
left1 = 0
right1 = 0

while left < right:
    sum1 = liquid[left]+liquid[right]
    
    if abs(sum1) < abs(min1):
        min1 = sum1
        left1 = liquid[left]
        right1 = liquid[right]
        
    if sum1 == 0:
        break
    
    elif sum1 > 0:
        right -= 1
    
    else:
        left += 1
        
print(left1, right1)