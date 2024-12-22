n = int(input())

for _ in range(n):
    quiz = input()
    scores = []
    cnt = 0
    for x in quiz:
        if x == 'O':
            cnt += 1
            scores.append(cnt)
        else:
            cnt = 0
            scores.append(cnt)
            
    print(sum(scores))