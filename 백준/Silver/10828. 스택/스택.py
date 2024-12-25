def stack(stack, command):
    command1 = command.split(' ')
    if command1[0] == 'push':
        num = int(command1[1])
        stack.append(num)
    elif command1[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif command1[0] == 'size':            
        print(len(stack))
    elif command1[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command1[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    else:
        pass
    
input1 = int(input())

stack1 = []
for i in range(input1):
    stack(stack1, input())