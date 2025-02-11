n = int(input())

power = 1
while power*2 <= n:
    power *= 2
    
if n == power:
    print(n)
else:
    print((n-power)*2)