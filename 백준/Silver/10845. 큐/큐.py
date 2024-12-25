def queue(queue, command):
    command1 = command.split(' ')
    if command1[0] == 'push':
        queue.append(int(command1[1]))
    elif command1[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif command1[0] == 'size':
        print(len(queue))            
        pass
    elif command1[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command1[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command1[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        pass
    
input1 = int(input())

queue1 = []
for i in range(input1):
    queue(queue1, input())