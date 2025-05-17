str1 = input().strip()

alphabet = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}

for s in str1:
    alphabet[s] += 1
    
print(*alphabet.values())