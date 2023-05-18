T = int(input())
for _ in range(T):
    t = int(input())
    scores = list(map(int, input().split()))
    arr = [0 for _ in range(1001)]

    for score in scores:
        arr[score] += 1

    arr.reverse()
    print('#' + str(t), 1000 - arr.index(max(arr)))