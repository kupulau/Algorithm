import sys
input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
    
announcement = []
for _ in range(5):
    announcement.append(list(map(int, input().split())))
    
announcement = [col for row in announcement for col in row]

def find_index(matrix, value):
    for i, row in enumerate(matrix):
        if value in row:
            return (i, row.index(value))
        
for index, v in enumerate(announcement):
    bingo_count = 0
    idx = find_index(board, v)
    board[idx[0]][idx[1]] = True
    
    # row-wise
    for i in range(5):
        if board[i] == [True, True, True, True, True]:
            bingo_count += 1
    
    if bingo_count >= 3:
        print(index+1)
        break
    
    # column-wise
    for i in range(5):
        cnt = 0
        for j in range(5):
            if board[j][i] == True:
                cnt += 1
        if cnt == 5:
            bingo_count += 1
    
    if bingo_count >= 3:
        print(index+1)
        break

    # diagonal-1
    cnt = 0
    for i in range(5):
        if board[i][i] == True:
            cnt += 1         
            #if cnt == 5:
            #    return True
    if cnt == 5:
        bingo_count += 1
        
    if bingo_count >= 3:
        print(index+1)
        break
    
    #diagonal-2
    cnt = 0
    for i in range(5):
        if board[i][4-i] == True:
            cnt += 1
    if cnt == 5:
        bingo_count += 1
        
    if bingo_count >= 3:
        print(index+1)
        break