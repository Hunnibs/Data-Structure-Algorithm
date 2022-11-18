def sol(x,y):
    if arr[y][x] == 1 and visited[y][x] == 0:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            visited[y][x] = 1

            if arr[ny][nx] == 1 and visited[ny][nx] == 0:
                sol(nx, ny)
    return

# input
dx = [1, -1, 0 , 0]
dy = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = []
    visited = []

    for i in range(N):
        arr.append([])
        visited.append([])
        for _ in range(M):
            arr[i].append(0)
            visited[i].append(0)

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                sol(j, i)
                cnt += 1

    print(cnt)