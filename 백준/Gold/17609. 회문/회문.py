def is_palindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def pseudo_palindrome(string):
    left, right = 0, len(string)-1
    while left < right:
        if string[left] != string[right]:
            if is_palindrome(string, left+1, right) or is_palindrome(string, left, right-1):
                return 1
            else:
                return 2     
        left += 1
        right -= 1    
    
            
t = int(input())
for _ in range(t):
    string = input()
    if is_palindrome(string, 0, len(string)-1):
        print(0)
        continue
    else:
        print(pseudo_palindrome(string))     