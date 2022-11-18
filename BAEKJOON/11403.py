# Floyd & warshall Algorithm

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if arr[i][k] and arr[k][j]:
                    arr[i][j] = 1

# input
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
floyd()
for row in arr:
    print(*row)

