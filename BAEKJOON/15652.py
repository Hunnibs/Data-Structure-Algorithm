def sol(result, tmp):
    if len(result) == M:
        for num in result:
            print(num, end= " ")
        print()
        return

    for i in range(tmp, N+1):
        result.append(i)
        sol(result, i)
        result.pop()

N, M = map(int, input().split())

result = []
sol(result, 1)