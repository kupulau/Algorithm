string = input().strip().lower()
spellings = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}

for i in string:
    spellings[i] += 1
    
max1 = max(spellings.values())
maxs = [k for k, v in spellings.items() if v==max1]

if len(maxs) >= 2:
    print('?')
else:
    print(maxs[0].upper())