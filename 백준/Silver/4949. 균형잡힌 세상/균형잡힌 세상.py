while True:
    str1 = input()
    if str1==".":
        break
    list1 = []   
    for s in str1:
        if s == "(" or s == "[":
            list1.append(s)
        elif s == ")":
            if len(list1)!=0 and list1[-1]=="(":
                list1.pop()
            else:
                list1.append(s)
        elif s == "]":
            if len(list1)!=0 and list1[-1]=="[":
                list1.pop()
            else:
                list1.append(s)

    if len(list1)==0:
        print('yes')
    else:
        print('no')