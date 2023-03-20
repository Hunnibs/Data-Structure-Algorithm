import sys
from collections import deque

def BFS():
    while queue:
        h, y, x = queue.popleft()
        for i in range(4):  # 상하좌우
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >= 0 and ny < N and nx >= 0 and nx < M:
                if totalBox[h][ny][nx] == 0:
                    totalBox[h][ny][nx] = 1
                    queue.append((h, ny, nx))
                    visited[h][ny][nx] = visited[h][y][x] + 1


        for i in range(2):  # 위 아래
            nh = h + dh[i]
            if nh >= 0 and nh < H:
                if totalBox[nh][y][x] == 0:
                    totalBox[nh][y][x] = 1
                    queue.append((nh, y, x))
                    visited[nh][y][x] = visited[h][y][x] + 1

# input
input = sys.stdin.readline
M, N, H = map(int, input().split())

totalBox = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    totalBox.append(box)
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dh = [1, -1]

queue = deque()
check = 0

for h in range(H):
    for y in range(N):
        for x in range(M):
            if totalBox[h][y][x] == 1:
                queue.append((h, y, x))

            if totalBox[h][y][x] == 0:
                check += 1

if check == 0:  # 다 익었다면
    print(0)
else:
    BFS()
    Max = 0
    for h in range(H):
        if Max == -1:
            break
        for y in range(N):
            if totalBox[h][y].count(0):
                Max = -1
                break
            Max = max(Max, max(visited[h][y]))

    print(Max)