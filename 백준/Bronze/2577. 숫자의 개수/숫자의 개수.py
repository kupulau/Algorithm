nums = []
for _ in range(3):
    n = int(input())
    nums.append(n)
    
multiply = nums[0]*nums[1]*nums[2]
multiply = str(multiply)

for i in range(10):
    print(multiply.count(str(i)))