import sys
input = sys.stdin.readline

m = int(input())

sum1 = 0
xor1 = 0
for _ in range(m):
    calc = input().split()
    if calc[0] == '1':
        sum1 += int(calc[1])
        xor1 ^= int(calc[1])
    elif calc[0] == '2':
        sum1 -= int(calc[1])
        xor1 ^= int(calc[1])
    elif calc[0] == '3':
        print(sum1)  
    elif calc[0] == '4':
        print(xor1)