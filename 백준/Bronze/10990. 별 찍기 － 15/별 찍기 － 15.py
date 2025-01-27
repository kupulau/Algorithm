n = int(input())

if n == 1:
    print('*')
else:
    print(' '*(n-1)+'*')
    for i in range(0, n-1):
        print(' '*(n-2-i)+'*'+' '*(2*i+1) + '*')