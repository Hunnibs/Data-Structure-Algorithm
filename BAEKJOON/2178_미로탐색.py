import sys
import math
from collections import deque

# input
input = sys.stdin.readline

maze = []
N, M = map(int, input().split())

for _ in range(N):
    maze.append(list(map(int, input().rstrip())))

# main
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [[math.inf for _ in range(M)] for _ in range(N)]
deque = deque()

deque.append([0, 0])
visited[0][0] = 1

status = 0

while deque:
    x, y = deque.popleft()

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < N and ty >= 0 and ty < M:
            if maze[tx][ty] == 1 and visited[tx][ty] == math.inf:
                visited[tx][ty] = min(visited[tx][ty], visited[x][y] + 1)
                deque.append([tx, ty])

            if tx == N-1 and ty == M-1:
                status = 1
                break

    if status:
        print(visited[N-1][M-1])
        break
