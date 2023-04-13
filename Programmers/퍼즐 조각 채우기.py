import copy


def solution(game_board, table):
    answer = 0
    N = len(game_board)
    blocks = []

    for x in range(N):
        for y in range(N):
            if game_board[x][y] == 0:
                blocks.append(check(game_board, x, y, [0, 0], 0))

    for i in range(4):
        if i != 0:
            table = turn(table)

        tmp_table = copy.deepcopy(table)
        for x in range(N):
            for y in range(N):
                if tmp_table[x][y] == 1:
                    block = check(tmp_table, x, y, [0, 0], 1)
                    if block in blocks:
                        answer += len(block)
                        blocks.remove(block)
                        table = copy.deepcopy(tmp_table)
                    else:
                        tmp_table = copy.deepcopy(table)

    return answer


def check(board, x, y, coordinate, num):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    result = [coordinate]
    board[x][y] = 2

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < len(board) and ty >= 0 and ty < len(board):
            if board[tx][ty] == num:
                result += check(board, tx, ty, [coordinate[0] + dx[i], coordinate[1] + dy[i]], num)

    return result


def turn(table):
    tmp = copy.deepcopy(table)
    N = len(table)

    for x in range(N):
        for y in range(N):
            tmp[x][y] = table[N - y - 1][x]

    return tmp
