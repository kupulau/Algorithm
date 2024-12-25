n = int(input())

def winner(n):
    if n%2 == 0:
        win = 'CY'
    else:
        win = 'SK'
    return win

print(winner(n))