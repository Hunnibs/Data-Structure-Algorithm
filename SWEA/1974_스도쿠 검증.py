T = int(input())
for t in range(1, T+1):
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    status = 1

    # 가로줄 검사
    for i in range(9):
        arr = set(board[i])
        if len(arr) != len(board[i]):
            status = 0
            break

    if status == 0:
        print('#' + str(t), status)
        continue

    # 세로줄 검사
    for y in range(9):
        arr = []
        for x in range(9):
            arr.append(board[x][y])
        arr2 = set(arr)
        if len(arr) != len(arr2):
            status = 0
            break

    if status == 0:
        print('#' + str(t), status)
        continue

    # 박스 검사
    index = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            index.append([i, j])

    for i, j in index:
        arr = []
        for x in range(i, i+3):
            for y in range(j, j+3):
                arr.append(board[x][y])
        arr2 = set(arr)
        if len(arr) != len(arr2):
            status = 0
            break

    print('#' + str(t), status)