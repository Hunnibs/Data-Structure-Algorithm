# input
N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

# main
cnt = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break

    if arr[i] > K:
        continue
    else:
        tmp = K // arr[i]
        cnt += tmp
        K = K - (arr[i] * tmp)

print(cnt)