input1 = int(input())

def VPS(str1):
    stack = []
    for s in str1:
        if s == '(':
            stack.append(s)
        else:    # s ==')'
            if len(stack)==0:
                print('NO')
                break
            else:
                stack.pop()
    else:      
        if len(stack)==0:
            print('YES')
        else:
            print('NO')

for i in range(input1):
    VPS(input())