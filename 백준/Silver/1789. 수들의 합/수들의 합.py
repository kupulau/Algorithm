input1 = int(input())

intsum = 0
i = 0
while True:
    i += 1
    intsum += i
    if intsum > input1:   
        break

print(i-1)