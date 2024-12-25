n = int(input())

def bamyanggang(n):
    if n == 1:
        return 10
    else:
        repeat = 1
        cnt = 0
        while repeat < n+1:
            cnt += 1
            repeat *= 2
        return cnt + 9     # first daldidalgo (8) + final n (1)

print(bamyanggang(n))