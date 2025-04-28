import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

blue = 0
white = 0

def divide(x, y, size):
    global blue, white

    first_color = paper[y][x]
    all_same = True

    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != first_color:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        if first_color == 0:
            white += 1
        else:
            blue += 1
    else:
        half = size // 2
        divide(x, y, half)
        divide(x + half, y, half)
        divide(x, y + half, half)
        divide(x + half, y + half, half)

divide(0, 0, n)

print(white)
print(blue)