import sys

input = sys.stdin.readline

def sol(i, sum):
    for x in range(i, N):
        for y in range(M):
            if visited[x][y]:
                continue

            if x+1 < N and y-1 >= 0 and not visited[x+1][y] and not visited[x][y-1]:
                visited[x][y] = 1
                visited[x+1][y] = 1
                visited[x][y-1] = 1
                sol(x, sum + board[x][y] * 2 + board[x+1][y] + board[x][y-1])
                visited[x][y] = 0
                visited[x+1][y] = 0
                visited[x][y-1] = 0

            if x-1 >= 0 and y-1 >= 0 and not visited[x-1][y] and not visited[x][y-1]:
                visited[x][y] = 1
                visited[x-1][y] = 1
                visited[x][y-1] = 1
                sol(x, sum + board[x][y] * 2 + board[x-1][y] + board[x][y-1])
                visited[x][y] = 0
                visited[x-1][y] = 0
                visited[x][y-1] = 0

            if x-1 >= 0 and y+1 < M and not visited[x-1][y] and not visited[x][y+1]:
                visited[x][y] = 1
                visited[x-1][y] = 1
                visited[x][y+1] = 1
                sol(x, sum + board[x][y] * 2 + board[x-1][y] + board[x][y+1])
                visited[x][y] = 0
                visited[x-1][y] = 0
                visited[x][y+1] = 0

            if x+1 < N and y+1 < M and not visited[x+1][y] and not visited[x][y+1]:
                visited[x][y] = 1
                visited[x+1][y] = 1
                visited[x][y+1] = 1
                sol(x, sum + board[x][y] * 2 + board[x+1][y] + board[x][y+1])
                visited[x][y] = 0
                visited[x+1][y] = 0
                visited[x][y+1] = 0

    result.append(sum)

# input
N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# main
visited = [[0 for _ in range(M)] for _ in range(N)]
result = []
if N == 1 and M == 1:  # 부메랑을 만들 수 없는 경우
    print(0)
else:
    for x in range(N):
        for y in range(M):
            sol(x, 0)

    print(max(result))