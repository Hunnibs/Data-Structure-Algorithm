import sys

# input
input = sys.stdin.readline

N, C = map(int, input().split())
H = []
for _ in range(N):
    H.append(int(input()))

# main
H.sort()
dist = 0
l, r = 1, H[-1]
while l <= r:
    min_dist = H[-1]
    mid = (l+r) // 2
    current = H[0]
    count = 1
    for i in range(1, N):
        if count == C:
            break
        if current + mid <= H[i]:
            count += 1
            min_dist = min(min_dist, H[i]-current)
            current = H[i]

    if count < C:
        r = mid - 1
    elif count == C:
        l = mid + 1
        dist = min_dist

print(dist)