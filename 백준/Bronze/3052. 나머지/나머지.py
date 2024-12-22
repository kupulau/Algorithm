rest = []
for _ in range(10):
    n = int(input())
    rest.append(n%42)
    
rest = set(rest)
print(len(rest))