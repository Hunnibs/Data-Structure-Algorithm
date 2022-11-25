# input
N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
tmp = M
result = 0

for i in range(N):
    for j in range(i+1, N, 1):
        for p in range(j+1, N, 1):
            Max = arr[i] + arr[j] + arr[p]
            if Max > M:
                break
            if M-Max < tmp:
                tmp = M-Max
                result = Max

print(result)