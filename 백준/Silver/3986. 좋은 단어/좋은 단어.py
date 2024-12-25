input1 = int(input())

good = 0
for i in range(input1):
    str1 = input()
    stack = []
    for s in str1:
        if len(stack)==0:
            stack.append(s)
        else:
            if s == stack[-1]:   # A & A or B & B
                stack.pop()
            else:    # A & B or B & A
                stack.append(s)
    if len(stack)==0:
        good += 1
    else:
        pass
    
print(good)