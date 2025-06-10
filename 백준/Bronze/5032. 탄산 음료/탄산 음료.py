e, f, c = map(int, input().split())

answer = 0
empty = e+f
while empty >= c:
    new = empty//c
    answer += new
    empty -= new*c
    empty += new

print(answer)    