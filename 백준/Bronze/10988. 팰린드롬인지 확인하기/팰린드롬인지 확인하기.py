def IsPalindrome(string):
    if string == string[::-1]:
        return 1
    else:
        return 0
    
string1 = input().strip()
print(IsPalindrome(string1))