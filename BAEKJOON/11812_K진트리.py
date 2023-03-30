import sys

def find(x, y):
    total = 0
    while x != y:
        if x > y:
            x = (x-2) // K + 1
            total += 1

        else:
            y = (y-2) // K + 1
            total += 1

    return total

# input
input = sys.stdin.readline

N, K, Q = map(int, input().split())

for _ in range(Q):
    x, y = map(int, input().split())
    if K == 1:
        print(abs(x-y))
    else:
        print(find(x, y))
