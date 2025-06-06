def draw(n, arr, x, y):
    size = 4*n - 3
    # 위, 아래
    for i in range(size):
        arr[x][y+i] = '*'
        arr[x+size-1][y+i] = '*'
    # 왼쪽, 오른쪽
    for i in range(1, size-1):
        arr[x+i][y] = '*'
        arr[x+i][y+size-1] = '*'
    # 재귀
    if n > 1:
        draw(n-1, arr, x+2, y+2)

n = int(input())
size = 4*n - 3
arr = [[' ']*size for _ in range(size)]
draw(n, arr, 0, 0)
for line in arr:
    print(''.join(line))