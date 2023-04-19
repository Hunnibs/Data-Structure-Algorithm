import copy
import sys
from collections import deque

def makeWall(i, count):
    if count == 3:
        result.append(bfs())
        return

    for x in range(i, N):
        for y in range(M):
            if lab[x][y] == 0:
                lab[x][y] = 1
                makeWall(x, count+1)
                lab[x][y] = 0

def bfs():
    virus_test = copy.deepcopy(virus)
    lab_test = copy.deepcopy(lab)

    visited = [[0 for _ in range(M)] for _ in range(N)]

    while virus_test:
        x, y = virus_test.popleft()
        visited[x][y] = 1

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx >= 0 and tx < N and ty >= 0 and ty < M:
                if lab_test[tx][ty] == 0 and not visited[tx][ty]:
                    lab_test[tx][ty] = 2
                    virus_test.append([tx, ty])
    return check_safetyZone(lab_test)

def check_safetyZone(lab_test):
    count = 0

    for x in range(N):
        for y in range(M):
            if lab_test[x][y] == 0:
                count += 1

    return count

# input
input = sys.stdin.readline

N, M = map(int, input().split())

lab = []
for _ in range(N):
    lab.append(list(map(int, input().split())))

# main
dx = [0 , 0, -1, 1]
dy = [1, -1, 0, 0]

# 바이러스 위치
virus = deque()
for x in range(N):
    for y in range(M):
        if lab[x][y] == 2:
            virus.append([x, y])

result = []
makeWall(0, 0)
print(max(result))