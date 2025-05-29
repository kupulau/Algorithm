a, b, c = map(int, input().split())

if len(set([a, b, c])) == 1:
    print(10000+a*1000)
    pass
elif len(set([a, b, c])) == 2:
    max1 = [x for x in [a, b, c] if [a, b, c].count(x)==2][0]
    print(1000+max1*100)
else:
    max1 = max(a, b, c)
    print(max1*100)