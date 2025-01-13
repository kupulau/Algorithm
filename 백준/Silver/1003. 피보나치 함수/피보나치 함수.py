cnt0 = [0]*41
cnt1 = [0]*41

cnt0[0] = 1
cnt1[1] = 1

def fibo(n):
    for i in range(2, n+1):
        cnt0[i] = cnt0[i-1]+cnt0[i-2]
        cnt1[i] = cnt1[i-1]+cnt1[i-2]
        
t = int(input())

for _ in range(t):
    n = int(input())
    fibo(n)
    print(cnt0[n], cnt1[n])