import sys
input = sys.stdin.readline

name1 = input().strip()
name2 = input().strip()

stroke = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
strokes = {chr(k):v for k, v in zip(range(ord('A'), ord('Z')+1), stroke)}

combi = "".join([x+y for x, y in zip(name1, name2)])
combi = [strokes[x] for x in combi]

score = combi
while len(score) > 2:
    score = [(score[i] + score[i+1]) % 10 for i in range(len(score) - 1)]

print(f"{score[0]}{score[1]}")