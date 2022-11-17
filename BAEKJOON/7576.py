from collections import deque

def BFS():
    Max = 0

    queue = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append((j, i))
                visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:  # 벽일 경우
                continue

            if visited[ny][nx] != 0:
                continue

            if arr[ny][nx] == 0:
                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1
                arr[ny][nx] = 1
                Max = visited[ny][nx]

    return Max

# input
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]  # 동서남북 이동, x축
dy = [0, 0, -1, 1]  # 동서남북 이동, y축

visited = []
for i in range(N):
    visited.append([])
    for j in range(M):
        visited[i].append(0)

Max = BFS()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            Max = -1
            break

print(Max)