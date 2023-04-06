import sys

# input
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

# main
dp = [1 for _ in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if line[i] > line[j]:
            continue
        else:
            dp[i+1] = max(dp[i+1], 1+dp[j+1])
print(max(dp))