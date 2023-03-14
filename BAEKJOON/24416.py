import sys
input = sys.stdin.readline

def fib(n):
    global count1
    if n == 1 or n ==2:
        count1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global count2
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        count2 += 1
        dp[i] = dp[i-1] + dp[i-2]

n = int(input())
dp = [0 for _ in range(n+1)]

count1, count2 = 0, 0
fib(n)
fibonacci(n)

print(count1, count2)