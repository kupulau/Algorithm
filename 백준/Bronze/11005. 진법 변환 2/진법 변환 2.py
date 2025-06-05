n, B = map(int, input().split())

remainder = []
while n > 0:
    remainder.append(n%B)
    n = n // B
    
dict1 = {k+10:chr(v) for k, v in zip(range(26), range(ord('A'), ord('Z') + 1))}   

answer = ""

for x in reversed(remainder):
    if x >= 10:
        answer += dict1[x]
    else:
        answer += str(x)
    
print(answer)