T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    x = (N // H) + 1
    y = N % H
    if y == 0:
        y = H
        x -= 1
    print(y * 100 + x)