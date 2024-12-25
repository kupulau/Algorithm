def mars_math(equation):
    equation = equation.replace('@', '*3')
    equation = equation.replace('%', '+5')
    equation = equation.replace('#', '-7')
    
    split = equation.split(' ')
    result = split[0]
    for i in range(1, len(split)):
        result = eval(str(result)+split[i])

    return format(float(result), '.2f')

input1 = int(input())

for a in range(input1):
    print(mars_math(input()))