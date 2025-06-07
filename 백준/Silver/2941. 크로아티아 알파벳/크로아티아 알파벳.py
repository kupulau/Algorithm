word = input().strip()

croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

cnt = 0
while len(word) > 0:
    now = word[0:3]
    if now == "dz=":
        cnt += 1
        word = word[3:]
    else:
        now = word[0:2]
        if now in croatian:
            cnt += 1
            word = word[2:]
        else:
            cnt += 1
            word = word[1:]
            
print(cnt)