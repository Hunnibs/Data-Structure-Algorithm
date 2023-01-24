# input
n = int(input())

# main
dp = [0,1]
for i in range(2, n+1):
    minValue = 5
    for j in range(1, (i ** 2) + 1):
        minValue = min(minValue, dp[i - j ** 2])
    dp.append(minValue)

print(dp[n])