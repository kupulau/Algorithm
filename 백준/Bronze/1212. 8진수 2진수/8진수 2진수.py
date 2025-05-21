oct = input().strip()
ten = int(oct, 8)
answer = bin(ten)[2:]
print(int(answer))