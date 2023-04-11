import sys

# input
input = sys.stdin.readline

N, K = map(int, input().split())
weight = []
value = []

for _ in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

# main
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    V = value[i-1]
    W = weight[i-1]
    for j in range(1, K+1):
        if W > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-W] + V, dp[i-1][j])

print(dp[N][K])
