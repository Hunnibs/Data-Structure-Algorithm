for t in range(1, 11):
    count = int(input())
    height = list(map(int, input().split()))

    for _ in range(count):
        height.sort()
        height[0] += 1
        height[-1] -= 1

    print('#' + str(t), max(height)-min(height))