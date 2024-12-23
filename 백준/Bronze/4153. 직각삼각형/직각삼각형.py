while True:
    input1 = list(map(int, input().split()))
    if input1 == [0, 0, 0]:
        break
    else:
        input1.sort()
        if input1[2]**2 == input1[0]**2+input1[1]**2:
            print('right')
        else:
            print('wrong')