n = int(input())

def factorial(n):
    if n == 0:
        return 1
    else: # 1 <= n
        return n*factorial(n-1)
        
print(factorial(n))