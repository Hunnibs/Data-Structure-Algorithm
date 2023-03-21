import sys

def sol():
    if len(result) == M:
        result_str = list(map(str, result))
        print(' '.join(result_str))
        return

    for i in range(N):
        if visited[i] == 0:
            result.append(arr[i])
            visited[i] = 1
            sol()
            visited[i] = 0
            result.pop()

# input
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
visited = [0 for _ in range(N)]

arr.sort()
for i in range(N):
    result = []
    result.append(arr[i])
    visited[i] = 1
    sol()
    visited[i] = 0
