import copy
import sys
from collections import deque

def group(x, y, num):
    queue.append([x, y])
    size, rainbow = 0, 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if board[tx][ty] == 0 and not visited[tx][ty]:
                    size += 1
                    rainbow += 1
                    visited[tx][ty] = 1
                    queue.append([tx, ty])
                elif board[tx][ty] == num and not visited[tx][ty]:
                    size += 1
                    visited[tx][ty] = 1
                    queue.append([tx, ty])

    reset_rainbow()

    return size, rainbow

def destroy(sx, sy):
    queue.append([sx, sy])
    num = board[sx][sy]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if board[tx][ty] == 0 and not visited[tx][ty]:
                    visited[tx][ty] = 1
                    board[tx][ty] = -2
                    queue.append([tx, ty])
                elif board[tx][ty] == num and not visited[tx][ty]:
                    visited[tx][ty] = 1
                    board[tx][ty] = -2
                    queue.append([tx, ty])

def gravity():
    for x in range(N-2, -1, -1):
        for y in range(N-1, -1, -1):
            if board[x][y] >= 0:
                queue.append([x, y])
                while queue:
                    qx, qy = queue.popleft()
                    tx, ty = qx+1, qy
                    if 0 <= tx < N:
                        if board[tx][ty] == -2:
                            board[tx][ty] = board[qx][qy]
                            board[qx][qy] = -2
                            queue.append([tx, y])

def rotate():
    rotate_board = copy.deepcopy(board)
    for x in range(N):
        for y in range(N):
            board[x][y] = rotate_board[y][N-x-1]

def reset_rainbow():
    for x in range(N):
        for y in range(N):
            if visited[x][y] and board[x][y] == 0:
                visited[x][y] = 0

def block():
    global answer

    max_size, max_rainbow = 0, 0
    sx, sy = 0, 0
    for x in range(N):
        for y in range(N):
            if board[x][y] != -1 and board[x][y] != 0:
                if not visited[x][y] and board[x][y] > 0:
                    size, rainbow = group(x, y, board[x][y])
                    if size > max_size:
                        max_size = size
                        max_rainbow = rainbow
                        sx, sy = x, y
                    elif size == max_size and rainbow > max_rainbow:
                        max_rainbow = rainbow
                        sx, sy = x, y
                    elif size == max_size and rainbow == max_rainbow:
                        sx, sy = x, y

    if max_size < 2:
        return
    answer += (max_size ** 2)
    destroy(sx, sy)
    # print('___')
    # for i in range(N):
    #     print(board[i])
    gravity()
    # print('___')
    # for i in range(N):
    #     print(board[i])
    rotate()
    # print('___')
    # for i in range(N):
    #     print(board[i])
    gravity()
    # print('___')
    # for i in range(N):
    #     print(board[i])

# input
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# main
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
answer = 0
tmp = -1
while answer != tmp:
    tmp = answer
    visited = [[0 for _ in range(N)] for _ in range(N)]
    block()

print(answer)