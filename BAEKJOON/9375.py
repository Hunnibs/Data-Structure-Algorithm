def sum(i, tmp):
    global result

    plus = tmp
    for j in range(i, len(arr)):
        sum(j+1, tmp)
        plus = plus * arr[j]
        result += plus

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
    arr = []
    for num in dict.values():
        arr.append(num)

    result = 0
    for i in range(len(arr)):
        result += arr[i]
        sum(i+1, arr[i])

    print(result)