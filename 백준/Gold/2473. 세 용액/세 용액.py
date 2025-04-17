import sys
input = sys.stdin.readline

n = int(input())
liquids = sorted(list(map(int, input().split())))

def solution():
    a, b, c = 0, 0, 0
    minsum = float('inf')
    for i in range(n-2):
        left = i+1
        right = n-1
        while left < right:
            sum1 = liquids[i]+liquids[left]+liquids[right]
            
            if abs(sum1) < minsum:
                minsum = abs(sum1)
                a, b, c = liquids[i], liquids[left], liquids[right]
            
            if sum1 == 0:
                return a, b, c
            elif sum1 > 0:
                right -= 1
            else:    # sum1 < 0
                left += 1
    return a, b, c
    
print(*solution())