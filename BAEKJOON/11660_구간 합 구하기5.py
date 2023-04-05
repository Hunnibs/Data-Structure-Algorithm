import sys

# input
input = sys.stdin.readline

N, M = map(int, input().split())

T = []
for _ in range(N):
    T.append(list(map(int, input().split())))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, N+1):
        dp[x][y] = dp[x][y-1] + dp[x-1][y] - dp[x-1][y-1] + T[x-1][y-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])