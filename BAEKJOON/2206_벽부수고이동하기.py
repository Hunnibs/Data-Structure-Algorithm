import sys
sys.setrecursionlimit(10 ** 9)

def DFS(x, y, dist, hammer):
    global result

    if result < dist:
        return

    if x == N - 1 and y == M - 1:
        if dist < result:
            result = dist
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < M:
                if map[tx][ty] == 0 and not visited[tx][ty]:
                    visited[tx][ty] = 1
                    DFS(tx, ty, dist + 1, hammer)
                    visited[tx][ty] = 0
                elif map[tx][ty] == 1 and hammer:
                    visited[tx][ty] = 1
                    hammer = 0
                    DFS(tx, ty, dist + 1, hammer)
                    visited[tx][ty] = 0
                    hammer = 1

# input
input = sys.stdin.readline

N, M = map(int, input().split())
map = [(list(map(int, list(input().strip())))) for _ in range(N)]

# main
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = N * M
DFS(0, 0, 1, 1)

if result == N * M:
    print(-1)
else:
    print(result)
