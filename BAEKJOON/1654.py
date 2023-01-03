def MaxLan():
    global cnt

    cnt = 0

    for i in range(K):
        cnt += (lan[i] // mid)
    return cnt

# input
K, N = map(int, input().split())

lan = []
for _ in range(K):
    lan.append(int(input()))

# main
lan.sort()
left, right = 1, lan[-1]
mid = (lan[-1]+1) // 2
result = 0

while(left <= right):
    cnt = MaxLan()

    if cnt < N:
        right = mid-1
        mid = (left + right) // 2
    else:
        left = mid+1
        mid = (left + right) // 2

print(mid)