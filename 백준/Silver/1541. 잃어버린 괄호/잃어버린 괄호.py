import sys
input = sys.stdin.readline

eq = input()

nums = []

split1 = eq.split('-')

for x in split1:
    x1 = x.split('+')
    sum1 = 0
    for y in x1:
        y1 = int(y)
        sum1 += y1
    nums.append(sum1)        

answer = nums[0]
for i in range(1, len(nums)):
    answer -= nums[i]
    
print(answer)