import math 

n = int(input())
num = str(math.factorial(n))[::-1]

cnt = 0
for x in num:
    if x != '0':
        break
    else:
        cnt += 1
        
print(cnt)