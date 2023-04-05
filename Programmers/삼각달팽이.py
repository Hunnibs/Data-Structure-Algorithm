def solution(n):
    answer = []
    t = n
    cnt = n - 1
    h = 0
    num = 1

    arr = [[] for _ in range(n)]
    arr2 = [[] for _ in range(n)]
    while n > 0:
        print(n)
        if n == 1:
            print(1)
            arr[h].append(num)
            break

        for i in range(h, h + n - 1):
            arr[i].append(num)
            num += 1

        for _ in range(n - 1):
            arr[cnt].append(num)
            num += 1
        cnt -= 1

        for i in range(h + n - 1, h, -1):
            arr2[i].append(num)
            num += 1

        h += 2
        n -= 3
    for i in range(t):
        for num in arr[i]:
            answer.append(num)
        for j in range(len(arr2[i]) - 1, -1, -1):
            answer.append(arr2[i][j])

    return answer