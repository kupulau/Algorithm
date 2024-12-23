nums = []
for _ in range(9):
    nums.append(int(input()))
    
max1 = max(nums)
print(max1)
print(nums.index(max1)+1)