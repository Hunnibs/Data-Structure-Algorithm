import sys
from collections import deque

def BFS():
    while queue:
        x, y, hammer = queue.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < M:
                if hammer:
                    if map[tx][ty] == 0:
                        if not dist[tx][ty]:
                            dist[tx][ty] = dist[x][y] + 1
                            queue.append([tx, ty, 1])
                        else:
                            if dist[tx][ty] > dist[x][y] + 1:
                                dist[tx][ty] = dist[x][y] + 1
                                queue.append([tx, ty, 1])
                    else:
                        dist_noHam[tx][ty] = dist[x][y] + 1
                        queue.append([tx, ty, 0])

                else:
                    if map[tx][ty] == 0:
                        if not dist_noHam[tx][ty]:
                            dist_noHam[tx][ty] = dist_noHam[x][y] + 1
                            queue.append([tx, ty, 0])
                        else:
                            if dist_noHam[tx][ty] > dist_noHam[x][y] + 1:
                                dist_noHam[tx][ty] = dist_noHam[x][y] + 1
                                queue.append([tx, ty, 0])

# input
input = sys.stdin.readline

N, M = map(int, input().split())
map = [(list(map(int, list(input().strip())))) for _ in range(N)]

# main
dist = [[0 for _ in range(M)] for _ in range(N)]
dist_noHam = [[0 for _ in range(M)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append([0, 0, 1])
BFS()

ham = dist[N-1][M-1]
noHam = dist_noHam[N-1][M-1]

if ham and noHam:
    if ham > noHam:
        print(noHam+1)
    else:
        print(ham+1)
elif ham:
    print(ham+1)
elif noHam:
    print(noHam+1)
elif N == 1 and M == 1:
    print(1)
else:
    print(-1)