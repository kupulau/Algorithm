word = input()

alphabets = [chr(i) for i in range(97, 123)]

for _ in alphabets:
    try:
        answer = word.index(_)
        print(answer, end=" ")
    except:   # ValueError
        print(-1, end=" ")