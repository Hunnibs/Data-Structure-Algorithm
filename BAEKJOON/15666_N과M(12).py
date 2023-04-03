import sys

def sol(x):
    if len(result) == M:
        result_str = tuple(map(str, result))
        if result_str not in resultList:
            resultList.append(result_str)
            print(' '.join(result_str))
        return

    for i in range(x, N):
        result.append(arr[i])
        sol(i)
        result.pop()

# input
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# main
arr.sort()
result = []
resultList = []

sol(0)