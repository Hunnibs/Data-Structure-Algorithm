import sys
from collections import deque

def dust():
    for x in range(R):
        for y in range(C):
            if board[x][y] and board[x][y] != -1:
                q.append([x, y, board[x][y]])

def spread():
    while q:
        x, y, quantity = q.popleft()
        cnt = 0
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < R and 0 <= ty < C:
                if board[tx][ty] != -1:
                    board[tx][ty] += quantity // 5
                    cnt += 1
        board[x][y] = board[x][y] - (quantity // 5) * cnt

def air():
    for x in range(upx-1, 0, -1):
        board[x][0] = board[x-1][0]

    for x in range(dwx+1, R-1):
        board[x][0] = board[x+1][0]

    for y in range(C-1):
        board[0][y] = board[0][y+1]
        board[R-1][y] = board[R-1][y+1]

    for x in range(upx):
        board[x][C-1] = board[x+1][C-1]

    for x in range(R-1, dwx, -1):
        board[x][C-1] = board[x-1][C-1]

    for y in range(C-1, 0, -1):
        if board[upx][y-1] == -1:
            board[upx][y], board[dwx][y] = 0, 0
            break
        board[upx][y] = board[upx][y-1]
        board[dwx][y] = board[dwx][y-1]

# input
input = sys.stdin.readline

R, C, T = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(map(int, input().split())))

# main
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q = deque()

# 공기청정기 위치
for x in range(R):
    if board[x][0] == -1:
        upx = x
        dwx = x+1
        break

for _ in range(T):
    dust()
    spread()
    air()

result = 0
for x in range(R):
    for y in range(C):
        if board[x][y] and board[x][y] != -1:
            result += board[x][y]

print(result)