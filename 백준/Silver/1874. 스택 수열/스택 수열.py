import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
current = 1  

for _ in range(n):
    num = int(input())  
    
    while current <= num:  
        stack.append(current)
        result.append("+")
        current += 1
    
    if stack[-1] == num: 
        stack.pop()
        result.append("-")
    else: 
        print("NO")
        exit()

print("\n".join(result)) 