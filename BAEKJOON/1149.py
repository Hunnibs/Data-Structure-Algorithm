import sys

# input
input = sys.stdin.readline

N = int(input())

H = []
for _ in range(N):
    H.append(list(map(int, input().split())))

dp = [[0 for _ in range(3)] for _ in range(N)]

for y in range(N-1, -1, -1):
    for x in range(3):
        if y == N-1:
            dp[y][x] = H[y][x]
        else:
            if x == 0:  # Red
                dp[y][x] = min(H[y][x] + dp[y+1][x+1], H[y][x] + dp[y+1][x+2])
            if x == 1:  # Green
                dp[y][x] = min(H[y][x] + dp[y+1][x-1], H[y][x] + dp[y+1][x+1])
            if x == 2:  # Blue
                dp[y][x] = min(H[y][x] + dp[y+1][x-1], H[y][x] + dp[y+1][x-2])

print(min(dp[0]))