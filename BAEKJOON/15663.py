import sys

def sol():
    if len(result) == M:
        result_str = tuple(map(str, result))
        if result_str not in resultList:
            resultList.add(result_str)
            print(' '.join(result_str))
        return

    for i in range(N):
        if not visited[i]:
            result.append(arr[i])
            visited[i] = 1
            sol()
            result.pop()
            visited[i] = 0

# input
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
arr.append(0)
visited = [0 for _ in range(N)]
resultList = set()

for i in range(N):
    if arr[i] == arr[i-1]:
        continue
    result = []
    result.append(arr[i])
    visited[i] = 1
    sol()
    result.pop()
    visited[i] = 0