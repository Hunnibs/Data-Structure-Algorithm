def check(i):
    if i == 1:
        return False

    if i == 2 or i == 3:
        return True

    if i % 2 == 0 or i % 3 == 0:
        return False

    root = int(i ** 0.5) + 1
    for j in range(5, root):
        if i % j == 0:
            return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if check(i):
        print(i)
