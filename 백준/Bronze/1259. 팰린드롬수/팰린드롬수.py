while True:
    n = input()
    if n == '0':
        break
    else:
        inverse = n[::-1]
        if n == inverse:
            print('yes')
        else:
            print('no')