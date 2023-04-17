import sys

# input
input = sys.stdin.readline

N = int(input())
T = []
dp = []
for i in range(N):
    T.append(list(map(int, input().split())))
    dp.append([0 for _ in range(i+1)])

# main
for i in range(N):
    dp[N-1][i] = T[N-1][i]

for i in range(N-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = T[i][j] + max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])