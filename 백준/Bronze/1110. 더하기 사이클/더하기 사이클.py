def plus_cycle(int1):    # int1 in str
    if int(int1) < 10:
        step1 = int(int1)
    else:
        step1 = eval(int1[0]+'+'+int1[1])

    step2 = int1[-1]+str(step1)[-1]
    return step2     # str

num = input()
num1 = int(num)
i = 0
while True:
    num = plus_cycle(num)
    if int(num)==num1:
        break
    i += 1

print(i+1)