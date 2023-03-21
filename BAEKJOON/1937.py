import sys

def sol(y, x):
    if dp[y][x] != 1:
        return dp[y][x]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if Map[ny][nx] > Map[y][x]:
                dp[y][x] = max(dp[y][x], sol(ny, nx) + 1)

    return dp[y][x]

# input
input = sys.stdin.readline

n = int(input())

dp = [[1 for _ in range(n)] for _ in range(n)]
Map = []
for _ in range(n):
    Map.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for y in range(n):
    for x in range(n):
        sol(y, x)

Max = 0
for y in range(n):
    Max = max(Max, max(dp[y]))

print(dp)
print(Max)