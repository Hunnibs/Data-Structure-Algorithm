import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp = [[0 for _ in range(N)] for _ in range(N)]

for y in range(N):
    for x in range(y, -1, -1):
        # 숫자가 한개인 경우
        if x == y:
            dp[x][y] = 1
            continue
        # 두 개
        if x+1 == y:
            if nums[x] == nums[y]:
                dp[x][y] = 1
        # 세 개 이상
        elif nums[x] == nums[y] and dp[x+1][y-1]:
            dp[x][y] = 1

for _ in range(M):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])