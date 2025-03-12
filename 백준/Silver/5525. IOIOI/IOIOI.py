import sys
input = sys.stdin.readline

n = int(input())  
m = int(input())  
s = input().strip()  

count = 0 
i = 0  
pattern_length = 0  

while i < m - 1:
    if s[i] == 'I' and i + 1 < m and s[i + 1] == 'O': 
        if i + 2 < m and s[i + 2] == 'I':  
            pattern_length += 1
            if pattern_length >= n:  
                count += 1
            i += 2  
        else:
            pattern_length = 0  
            i += 1
    else:
        pattern_length = 0 
        i += 1

print(count)