import sys

# input
input = sys.stdin.readline

N, M = map(int, input().split())
T = list(map(int, input().split()))

# main
l, r = 0, max(T)
H = 0
while l <= r:
    mid = (l + r) // 2
    result = 0
    for tree in T:
        if tree > mid:
            result += (tree-mid)

    if result == M:
        H = mid
        break
    elif result < M:
        r = mid-1
    else:
        H = mid
        l = mid+1

print(H)