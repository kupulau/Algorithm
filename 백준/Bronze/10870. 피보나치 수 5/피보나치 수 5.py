n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:    # n >= 2
        return fibonacci(n-2)+fibonacci(n-1)
    
print(fibonacci(n))