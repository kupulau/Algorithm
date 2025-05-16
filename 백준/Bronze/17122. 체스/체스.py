t = int(input())

for _ in range(t):
    str1, str2 = input().split()
    
    if str1[0] == 'A' or str1[0] == 'C' or str1[0] == 'E' or str1[0] == 'G':
        if int(str1[1])%2 == 0:
            check1 = 'white'
        else:
            check1 = 'black'
            
    else:
        if int(str1[1])%2 == 0:
            check1 = 'black'
        else:
            check1 = 'white'
            
    a, b = int(str2)//8, int(str2)%8   # a+1 -> row , b -> column
    
    if b == 0:
        if a%2 == 1:
            check2 = 'white'
        else:
            check2 = 'black'
        
    else:
        if b%2 == 1:     #  A, C, E, G
            if (a+1)%2 == 1:
                check2 = 'black'
            else:
                check2 = 'white'
        else:
            if (a+1)%2 == 1:
                check2 = 'white'
            else:
                check2 = 'black'
    
    if check1 == check2:
        print('YES')
    else:
        print('NO')