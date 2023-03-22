import sys

def sol(i):
    if len(result) == M:
        result_str = list(map(str, result))
        print(' '.join(result_str))
        return

    for j in range(i, N):
        result.append(arr[j])
        sol(j)
        result.pop()

# input
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
for i in range(N):
    result = []
    result.append(arr[i])
    sol(i)
