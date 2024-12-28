a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a 

ans1 = gcd(a, b)

print(ans1)
print(ans1*(a//ans1)*(b//ans1))