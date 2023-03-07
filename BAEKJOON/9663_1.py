import sys
input = sys.stdin.readline

def sol(y):
    # 마지막 줄이라면 퀸을 놓을 수 있는 위치 확인 후 리턴
    if y == N-1:
        global count
        count += visited[y].count(0)
        return

    for x in range(N):
        if not visited[y][x]:
            for i in range(N):
                if y+i < N:
                    visited[y+i][x] += 1
                if y+abs(x-i) < N:
                    visited[y+abs(x-i)][i] += 1
            sol(y+1)
            for i in range(N):
                if y+i < N:
                    visited[y+i][x] -= 1
                if y+abs(x-i) < N:
                    visited[y+abs(x-i)][i] -= 1

# input
N = int(input())

# main
visited = [[0 for _ in range(N)] for _ in range(N)]
count = 0

sol(0)

print(count)