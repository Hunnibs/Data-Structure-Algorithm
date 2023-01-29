# input
T = int(input())
for _ in range(T):
    # input
    m = int(input())
    dict = {}
    for _ in range(m):
        a, b = input().split()
        if dict.get(b):
            dict[b] += 1
        else:
            dict[b] = 1

    # main
    result = 1
    for num in dict.values():
        result *= num+1

    print(result-1)