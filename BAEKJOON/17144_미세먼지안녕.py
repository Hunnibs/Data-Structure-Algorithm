import sys
from collections import deque

def dust():
    for x in range(R):
        for y in range(C):
            if map[x][y] and map[x][y] != -1:
                q.append([x, y, map[x][y]])

def spread():
    while q:
        x, y, quantity = q.popleft()
        cnt = 0
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < R and 0 <= ty < C:
                if map[tx][ty] and map[tx][ty] != -1:
                    map[tx][ty] += map[x][y] // 5
                    cnt += 1
        map[x][y] = map[x][y] - (map[x][y] // 5) * cnt

def air():
    for x in range(upx-1, 0, -1):
        map[x+1][0] = map[x][0]

    for x in range(dwx+1, 0, -1):
        map[x-1][0] = map[x][0]

    for y in range(C-2):
        map[0][y] = map[0][y+1]
        map[R-1][y] = map[R-1][y+1]

    for x in range(upx-1):
        map[x][C-1] = map[x+1][C-1]

    for x in range(dwx-1):
        map[x][C-1] = map[x+1][C-1]

    for y in range(C-1, -1, -1)

# input
input = sys.stdin.readline

R, C, T = map(int, input().split())

map = []
for _ in range(R):
    map.append(list(map(int, input().split())))

# main
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q = deque()

# 공기청정기 위치
for x in range(R):
    if map[x][0] == -1:
        upx = x
        dwx = x+1
        break

for _ in range(T):
    dust()
    spread()
    air()

