T = int(input())
for t in range(1, T+1):
    N = int(input())

    print('#' + str(t))

    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr[0][0] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    i = 0
    x, y = 0, 0
    for num in range(2, N*N+1):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
            if arr[x+dx[i]][y+dy[i]]:
                i += 1
                if i == 4:
                    i = 0
        else:

            i += 1
            if i == 4:
                i = 0
        x, y = x+dx[i], y+dy[i]
        arr[x][y] = num

    for i in range(N):
        for num in arr[i]:
            print(num, end=' ')
        print()