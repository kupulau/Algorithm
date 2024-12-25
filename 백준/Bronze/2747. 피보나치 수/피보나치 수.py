input1 = int(input())
             
list1 = [0 for x in range(input1+1)]
             
def Fibonacci(n):
    if n <= 2:
        return 1
    
    if list1[n]:
        return list1[n]
    
    list1[n] = Fibonacci(n-2)+Fibonacci(n-1)
    
    return list1[n]

print(Fibonacci(input1))