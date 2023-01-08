# input
n = int(input())

# main
dp = [0] * (n+1)
dp[1] = 1
if n > 1:
    dp[2] = 2

if n > 2:
    for i in range(3, n+1):
        dp[i] = sum(dp[i-2:i])
        
print(dp[n] % 10007)