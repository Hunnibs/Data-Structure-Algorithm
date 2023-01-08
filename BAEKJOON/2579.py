# input
N = int(input())

arr = [0]
dp = [0]
for _ in range(N):
    arr.append(int(input()))
    dp.append(0)

# main
if N == 1:
    print(arr[1])
elif N == 2:
    print(arr[1] + arr[2])
elif N == 3:
    print(arr[3] + max(arr[1], arr[2]))
else:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    dp[3] = arr[3] + max(arr[1], arr[2])

    for i in range(4, N+1):
        dp[i] = arr[i] + max(dp[i-2], arr[i-1] + dp[i-3])

    print(dp[N])