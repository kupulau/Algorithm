a, b, v = map(int, input().split())

i = (v-a)//(a-b)
rest = (v-a)%(a-b)

if rest == 0:
    print(i+1)
else:
    print(i+2)